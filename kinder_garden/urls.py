from django.urls import path
from .views import home, about, classes, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('classes/', classes, name='classes'),
    path('contact/', contact, name='contact'),
]