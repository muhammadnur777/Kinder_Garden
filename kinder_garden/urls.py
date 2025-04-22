from django.urls import path
from .views import home, about, classes

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('classes/', classes, name='classes'),
]