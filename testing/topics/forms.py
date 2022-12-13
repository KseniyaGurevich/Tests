from django import forms
from .models import Group, Test


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('name', 'group')
