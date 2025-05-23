from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Add new task...',
            'style': 'padding: 15px; font-size: 14px; width: 100%; border: none;'})
    )

    class Meta:
        model = Task
        fields = ['title']
