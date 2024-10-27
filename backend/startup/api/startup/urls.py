from django.urls import path

from .crud_api import startups_list, startups_detail, create_new_startup, delete_startup
from .export_api import export_startups


urlpatterns = [
    path('',startups_list, name='startups_list' ),
    path('<uuid:pk>/',startups_detail, name='startups_detail'),
    path('create/', create_new_startup, name='create_new_startup'),
    path('export/', export_startups, name='export_startups'),
    path('delete<uuid:pk>/', delete_startup, name='delete_startup')
]


