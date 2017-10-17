from django import forms
from django.contrib.auth.models import User
from django.views.generic import TemplateView,UpdateView

from .models import Student


class LoginForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'password']
