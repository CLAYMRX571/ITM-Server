"""
URL configuration for menu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from apps.account.views import Accountviews, lan_switch_account
from apps.cash.views import Cashviews, lan_switch_cash
from apps.home.views import Homeviews, lan_switch
from apps.host.views import Hostviews, lan_switch_host
from apps.payment.views import Paymentviews, lan_switch_payment
from apps.sertificat.views import Sertificatviews, lan_switch_sertificat
from apps.server.views import Serverviews, lan_switch_server

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('lan/account/<str:lan>/', lan_switch_account, name='lan_switch_account'),
    path('lan/cash/<str:lan>/', lan_switch_cash, name='lan_switch_cash'),
    path('lan/<str:lan>/', lan_switch, name='lan_switch'),
    path('lan/host/<str:lan>/', lan_switch_host, name='lan_switch_host'),
    path('lan/payment/<str:lan>/', lan_switch_payment, name='lan_switch_payment'),
    path('lan/sertificat/<str:lan>/', lan_switch_sertificat, name='lan_switch_sertificat'),
    path('lan/server/<str:lan>/', lan_switch_server, name='lan_switch_server'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('account/', Accountviews, name='account'),
    path('cash/', Cashviews, name='cash'),
    path('', Homeviews, name='home'),
    path('host/', Hostviews, name='host'),
    path('payment/', Paymentviews, name='payment'),
    path('sertificat/', Sertificatviews, name='sertificat'),
    path('server/', Serverviews, name='server'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
