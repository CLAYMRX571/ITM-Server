from modeltranslation.translator import register, TranslationOptions
from .models import Host

@register(Host)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)