from django.urls import path
from .views import index, importar, upload

urlpatterns = [
    path('', index, name='index'),
    path('importar/', importar, name='importar'),
    path('upload/', upload, name='upload')
]