from django import forms
from .models import Location
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ['user', 'tags']
