from django.contrib import admin
from .models import Banner, Classes






@admin.register(Classes)
class SchoolClassesAdmin(admin.ModelAdmin):
    list_display = ('lesson_name', )









