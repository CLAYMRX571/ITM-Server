from django.shortcuts import render, redirect
from .models import Server

def Serverviews(request):
    server = Server.objects.all()  

    context = {
        'server': server,
    }

    return render(request, 'server.html', context)

def lan_switch_server(request, lan):
    return redirect(f'/{lan}/server/')