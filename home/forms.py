from django import forms
from django.forms import ModelForm

from .models import Customer, RELIGION, GENDER


class CustomerCreateForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your name', 'required': 'required'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your email', 'required': 'required'}),
            'phone': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your phone', 'required': 'required'}),
            'dob': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'required': 'required', 'id': 'dob'}),
            'age': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your age', 'required': 'required'}),
            'address': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your address', 'required': 'required'}),
            'religion': forms.Select(choices=RELIGION, attrs={'class': 'form-control'}),
            'gender': forms.Select(choices=GENDER, attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'img-input', 'accept': 'image'}),
        }


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['slug']