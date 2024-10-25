from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from ...models import Startup
from .serializers import StartupSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def startups_list(request):
    startups = Startup.objects.all()

    # Filter
    category_ids = request.GET.getlist('category_ids', [])
    founder_ids = request.GET.getlist('founder_ids', [])
    batch_id = request.GET.get('batch_id', '')
    phase = request.GET.get('phase', '')
    status = request.GET.get('status', '')
    priority = request.GET.get('priority', '')

    for startup in startups:
        print(startup.name, startup.status)

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

    if priority:
        startups = startups.filter(priority=priority)

    serializer = StartupSerializer(startups, many=True)

    return JsonResponse({
        'data': serializer.data,
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def startups_detail(request, pk):
    try:
        startup = Startup.objects.get(pk=pk)
    except Startup.DoesNotExist:
        return JsonResponse({'error': 'Startup not found'}, status=404)

    serializer = StartupSerializer(startup, many=False)
    
    return JsonResponse(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_new_startup(request):
    serializer = StartupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    pitch_deck_file = request.FILES.get('pitch_deck')
    if pitch_deck_file and pitch_deck_file.size > 1 * 1024 * 1024:  # 1 MB limit
        return Response({"error": "Pitch deck file size must be under 1MB."}, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)