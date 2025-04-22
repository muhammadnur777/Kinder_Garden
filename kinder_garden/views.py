from django.shortcuts import render
from .models import Banner, SchoolClasses, PhotoGallery
from django.utils.translation import get_language

def home(request):
    banners = Banner.objects.all()
    classes = SchoolClasses.objects.all()
    return render(request, 'index.html', {
        'banners': banners,
        'classes': classes
    })

def about(request):
    return render(request, 'about.html') 

def classes(request):
    classes = SchoolClasses.objects.all()
    return render(request, 'classes.html', {
        'classes': classes
    })   


TRANSLATIONS = {
    'Rus tili': {'ru': 'Русский язык'},
    'Fizika': {'ru': 'Физика'},
    'Ingliz tili': {'ru': 'Английский язык'},
}


# def classes(request):
#     lang = get_language()
#     classes = SchoolClasses.objects.all()
#     context = {
#         'classes': classes,
#         'lang': lang,
#         'translations': TRANSLATIONS,
#     }
#     return render(request, 'your_template.html', context)
