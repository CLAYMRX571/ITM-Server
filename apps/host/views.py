from django.shortcuts import render, redirect
from .models import Host

def Hostviews(request):
    host = Host.objects.all()  

    context = {
        'host': host,
    }

    return render(request, 'host.html', context)

def lan_switch_host(request, lan):
    return redirect(f'/{lan}/host/')