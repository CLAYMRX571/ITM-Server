from django.contrib import admin
from django.db import models
from modeltranslation.admin import TranslationAdmin
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Account

@admin.register(Account)
class AccountAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }