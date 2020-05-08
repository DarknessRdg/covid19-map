from django.urls import path
from core import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('upload/', views.Upload.as_view(), name='upload')
]