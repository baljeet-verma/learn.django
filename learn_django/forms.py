
from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        max_length=60,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm'
        })
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=60,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm'
        })
    )
    email_address = forms.EmailField(
        label='Email Address',
        max_length=60,
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-sm'
        })
    )
    user_name = forms.CharField(
        label='User Name',
        min_length=8,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm'
        })
    )
    password = forms.CharField(
        label='Password',
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-sm'
        })
    )
    password_confirmation = forms.CharField(
        label='Confirm Password',
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-sm'
        })
    )