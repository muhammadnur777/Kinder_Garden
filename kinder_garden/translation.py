from modeltranslation.translator import register, TranslationOptions
from .models import Classes

@register(Classes)
class SchoolClassesTranslationOptions(TranslationOptions):
    fields = ('lesson_name',)
