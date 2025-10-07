from django.urls import path
from . import views

urlpatterns = [
    path('', views.Hostviews, name='host'),
]