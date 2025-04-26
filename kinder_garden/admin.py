from django.contrib import admin
from .models import Classes, Banner, PhotoGallery

# @admin.site.register(Banner)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass



@admin.register(Classes)
class SchoolClassesAdmin(admin.ModelAdmin):
    list_display = ('lesson_name', )

