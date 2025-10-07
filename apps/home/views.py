from django.shortcuts import render, redirect
from .models import Home

def Homeviews(request):
    home = Home.objects.all()  

    context = {
        'home': home,
    }

    return render(request, 'index.html', context)

def lan_switch(request, lan):
    return redirect(f'/{lan}/')