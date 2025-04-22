from django.contrib import admin
import kinder_garden.translation 
from .models import Banner, SchoolClasses, PhotoGallery
from modeltranslation.admin import TranslationAdmin


@admin.register(SchoolClasses)
class SchoolClassesAdmin(admin.ModelAdmin):
    list_display = ('lesson_name', )


admin.site.register(Banner)
# admin.site.register(SchoolClasses)





# @admin.register(SchoolClasses)
# class SchoolClassesAdmin(TranslationAdmin):
#     pass

