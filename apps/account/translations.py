from modeltranslation.translator import register, TranslationOptions
from .models import Account

@register(Account)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)