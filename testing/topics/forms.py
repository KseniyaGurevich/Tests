from django import forms
from .models import Group, Test, Question, Answer


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('name', 'group')


class AnswerForm(forms.Form):
    answer_check = forms.BooleanField(required=False)

    def clean_post(self):
        data = self.cleaned_data['answer_check']
        if data is False:
            raise forms.ValidationError('Выберите один вили несколько вариантов ответа')
        return data
