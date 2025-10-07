from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cashviews, name='cash'),
]