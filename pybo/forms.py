from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']