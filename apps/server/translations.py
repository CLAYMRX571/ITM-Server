from modeltranslation.translator import register, TranslationOptions
from .models import Server

@register(Server)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)