from django.shortcuts import render, redirect
from .models import Payment

def Paymentviews(request):
    payment = Payment.objects.all()  

    context = {
        'payment': payment,
    }

    return render(request, 'payment.html', context)

def lan_switch_payment(request, lan):
    return redirect(f'/{lan}/payment/')