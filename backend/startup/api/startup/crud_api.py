from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from ...models import Startup
from .serializers import StartupSerializer
from django.db.models import Case, When, Value, IntegerField
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from rest_framework.filters import SearchFilter


from .filter import StartupFilter

class StartupListView(generics.ListAPIView):
    queryset = Startup.objects.all()
    permission_classes = [AllowAny]
    serializer_class = StartupSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StartupFilter
    search_fields = ['$name'] 
 

class StartupDetailView(generics.RetrieveAPIView):
    queryset = Startup.objects.all()   
    serializer_class = StartupSerializer
    permission_classes = [AllowAny]  

    def get_object(self):
        try:
            startup = Startup.objects.get(pk=self.kwargs['pk'])
            return startup
        except Startup.DoesNotExist:
            raise Http404