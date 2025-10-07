from django.shortcuts import render, redirect
from .models import Domain

def Domainviews(request):
    domain = Domain.objects.all()  

    context = {
        'domain': domain,
    }

    return render(request, 'domain.html', context)

def lan_switch_domain(request, lan):
    return redirect(f'/{lan}/domain/')