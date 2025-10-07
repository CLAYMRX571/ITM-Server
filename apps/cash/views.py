from django.shortcuts import render, redirect
from .models import Cash

def Cashviews(request):
    cash = Cash.objects.all()  

    context = {
        'cash': cash,
    }

    return render(request, 'cash.html', context)

def lan_switch_cash(request, lan):
    return redirect(f'/{lan}/cash/')