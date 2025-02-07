from django.urls import path

from .api import StartupListView, StartupDetailView, CreateStartupView, StartupExportView
from .analytics import StartupAnalyticsView

urlpatterns = [
    path('', StartupListView.as_view(), name='startups-list'),
    path('<uuid:pk>', StartupDetailView.as_view(), name='startup-detail'),
    path('create', CreateStartupView.as_view(), name='startup-create'),
    path('export', StartupExportView.as_view(), name='startup-export'),
    path('analytics', StartupAnalyticsView.as_view(), name='startup-analytics'),
]

