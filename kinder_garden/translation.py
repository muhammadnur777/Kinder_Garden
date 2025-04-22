from modeltranslation.translator import register, TranslationOptions
from .models import SchoolClasses

@register(SchoolClasses)
class SchoolClassesTranslationOptions(TranslationOptions):
    fields = ('lesson_name',)
