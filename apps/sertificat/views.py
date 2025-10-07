from django.shortcuts import render, redirect
from .models import Sertificat

def Sertificatviews(request):
    sertificat = Sertificat.objects.all()  

    context = {
        'sertificat': sertificat,
    }

    return render(request, 'sertificat.html', context)

def lan_switch_sertificat(request, lan):
    return redirect(f'/{lan}/sertificat/')