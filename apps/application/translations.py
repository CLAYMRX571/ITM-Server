from modeltranslation.translator import register, TranslationOptions
from .models import Application

@register(Application)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)