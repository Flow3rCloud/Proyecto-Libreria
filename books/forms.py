from dataclasses import fields
from django import forms

from .models import Libro

class LibroForms(forms.ModelForm):

    class Meta:
        model=Libro
        fields='__all__'