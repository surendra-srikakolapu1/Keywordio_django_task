from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm


class BookModelForm(forms.ModelForm):

    class Meta:

        model = Book
        fields = '__all__'


class CategoryModelForm(forms.ModelForm):

    class Meta:

        model = Category
        fields = '__all__'


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')