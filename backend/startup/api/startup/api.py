from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated
from ...forms import StartupForm
from ...models import Startup, Founder, Category, Batch
from .serializers import StartupSerializer, BatchSerializer, FounderSerializer, CategorySerializer
from useraccount.models import User

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def startups_list(request):
    # Auth
    user = None
    try:
        token = request.META.get('HTTP_AUTHORIZATION', '').split('Bearer ')[1]
        token = AccessToken(token)
        user_id = token.payload['user_id']
        user = User.objects.get(pk=user_id)
    except Exception:
        user = None

    favorites = []
    startups = Startup.objects.all()

    # Filter
    is_favorites = request.GET.get('is_favorites', '')
    category_ids = request.GET.getlist('category_ids', [])
    founder_ids = request.GET.getlist('founder_ids', [])
    batch_id = request.GET.get('batch_id', '')
    phase = request.GET.get('phase', '')
    status = request.GET.get('status', '')

    # Filtering startups based on query parameters
    if category_ids:
        startups = startups.filter(categories__id__in=category_ids).distinct()

    if founder_ids:
        startups = startups.filter(founders__id__in=founder_ids).distinct()

    if batch_id:
        startups = startups.filter(batch_id=batch_id)

    if phase:
        startups = startups.filter(phase=phase)

    if status:
        startups = startups.filter(status=status)

    # Handle favorites
    if user:
        favorites = list(startups.filter(founders__in=[user]).values_list('id', flat=True))

    # Serialize the data
    serializer = StartupSerializer(startups, many=True)

    return JsonResponse({
        'data': serializer.data,
        'favorites': favorites
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def startups_detail(request, pk):
    try:
        startup = Startup.objects.get(pk=pk)
    except Startup.DoesNotExist:
        return JsonResponse({'error': 'Startup not found'}, status=404)

    serializer = StartupSerializer(startup, many=False)
    
    return JsonResponse(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensures that the user must be authenticated
def create_startup(request):
    form = StartupForm(request.POST, request.FILES)

    if form.is_valid():
        startup = form.save(commit=False)
        startup.founders.add(request.user)  # Assuming the user is the founder or you want to associate it with the user
        startup.save()

        return JsonResponse({'success': True, 'startup_id': str(startup.id)}, status=201)
    else:
        print('error', form.errors)
        return JsonResponse({'errors': form.errors.as_json()}, status=400)


