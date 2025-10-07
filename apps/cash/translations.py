from modeltranslation.translator import register, TranslationOptions
from .models import Cash

@register(Cash)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)