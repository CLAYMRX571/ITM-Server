from django.shortcuts import render, redirect
from .models import Account

def Accountviews(request):
    account = Account.objects.all()  

    context = {
        'account': account,
    }

    return render(request, 'account.html', context)

def lan_switch_account(request, lan):
    return redirect(f'/{lan}/account/')