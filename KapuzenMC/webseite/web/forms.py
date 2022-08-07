from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=35, label='Username Eintragen')
    password = forms.CharField(min_length=6, max_length=50,label='Passwort Eintargen', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email Eintragen')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Diesen Usernamen gibt es schon!')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Diese Email gibt es schon!')
        return email

class LoginForm(forms.Form):
    username = forms.CharField(max_length=35, label='Username Eintragen')
    password = forms.CharField(min_length=6, max_length=50, label='Passwort Eintargen', widget=forms.PasswordInput)
