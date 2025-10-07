from modeltranslation.translator import register, TranslationOptions
from .models import Payment

@register(Payment)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)