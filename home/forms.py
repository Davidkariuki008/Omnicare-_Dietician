from django import forms
from .models import Details


class DetailForm(forms.ModelForm):

    class Meta:
        model = Details
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Full Name'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Your Age'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Your Weight (in kg)'}),
            'height': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Your Height (in cms)'}),
            'activity': forms.Select(attrs={'class': 'form-control'}),
        }