from modeltranslation.translator import register, TranslationOptions
from .models import Domain

@register(Domain)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)