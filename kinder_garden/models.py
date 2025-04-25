from django.db import models

# Create your models here.

class Banner(models.Model):
    banner_image = models.ImageField(upload_to='images/', )


class Classes(models.Model):
    photo = models.ImageField(upload_to='images/')
    lesson_name = models.CharField(max_length=200)
    duration = models.IntegerField()
    children = models.CharField(max_length=100, null=True, blank=True)

class PhotoGallery(models.Model):
    photo = models.ImageField(upload_to='images/')