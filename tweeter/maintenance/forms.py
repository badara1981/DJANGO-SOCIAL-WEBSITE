from django import forms
from .models import Problem


class NewProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = '__all__'
        exclude = ('date_solve', 'solve')

        widgets = {
                'user': forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
                'message': forms.Textarea(attrs={'class': 'form-control'}),
                'room_name': forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
                'date_publish': forms.DateInput(attrs={'class':'form-control', 'type': 'datetime-local'}),
            }