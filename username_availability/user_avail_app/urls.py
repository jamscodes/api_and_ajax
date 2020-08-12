from django.urls import path, include
from . import views, actions

urlpatterns = [
    path('', views.index),
    path('register/', actions.register),
    path('username/', actions.username)
]