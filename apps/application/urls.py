from django.urls import path
from . import views

urlpatterns = [
    path('', views.Applicationviews, name='application'),
]