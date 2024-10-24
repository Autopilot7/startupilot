from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Startup
from ..serializers import StartupSerializer

class StartupListView(generics.ListAPIView):
    serializer_class = StartupSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['phase', 'status', 'priority', 'categories']

    def get_queryset(self):
        queryset = Startup.objects.all()

        # Custom filtering logic (optional if using filterset_fields)
        phase = self.request.query_params.get('phase', None)
        status_param = self.request.query_params.get('status', None)
        priority = self.request.query_params.get('priority', None)
        batch = self.request.query_params.get('batch', None)  # Assuming 'batch' is an additional field
        categories = self.request.query_params.getlist('categories', None)

        if phase:
            queryset = queryset.filter(phase=phase)
        if status_param:
            queryset = queryset.filter(status=status_param)
        if priority:
            queryset = queryset.filter(priority=priority)
        if categories:
            queryset = queryset.filter(categories__id__in=categories)
        if batch:
            queryset = queryset.filter(batch=batch)  # Assuming a 'batch' field is available

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = StartupSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)