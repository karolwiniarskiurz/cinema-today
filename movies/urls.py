from django.urls import path

from . import views

urlpatterns = [
    path('movies/<int:id>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]
