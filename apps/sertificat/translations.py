from modeltranslation.translator import register, TranslationOptions
from .models import Sertificat

@register(Sertificat)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)