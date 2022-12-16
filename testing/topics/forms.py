from django import forms
from .models import Group, Test, Question, Answer


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('name', 'group')


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('name', 'question', 'check')
        readonly_fields = ('name', )

