from django.urls import path, include
from schoolmeal import views

urlpatterns = [
    path('', views.index),
]
