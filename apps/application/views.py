from django.shortcuts import render, redirect
from .models import Application

def Applicationviews(request):
    application = Application.objects.all()  

    context = {
        'application': application,
    }

    return render(request, 'application.html', context)

def lan_switch_application(request, lan):
    return redirect(f'/{lan}/application/')