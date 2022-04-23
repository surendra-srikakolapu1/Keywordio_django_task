from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(
        Category, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Resume_download_file(models.Model):

    file_name = models.CharField(max_length=50)
    file_upload = models.FileField(upload_to='upload_download_files')

    def __str__(self):
        return self.file_name





class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)