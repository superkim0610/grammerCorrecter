from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('', views.index),
    path('check/', views.check),
    path('result/', views.result)
]
