from django.urls import path, include
from translator import views

urlpatterns = [
    path('', views.index),
    path('develop/', views.develop)
]
