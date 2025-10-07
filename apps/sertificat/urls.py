from django.urls import path
from . import views

urlpatterns = [
    path('', views.Sertificatviews, name='sertificat'),
]