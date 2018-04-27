from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from bootstrap_datepicker.widgets import DatePicker

from.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class InscriptionForm(forms.Form):
    #first_name = forms.CharField(label='Prenoms', max_length=250)
    username = forms.CharField(label='Utilisateur', min_length=6, max_length=150)
    email = forms.EmailField()
    password1 = forms.CharField(label='Mot de Passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmer le Mot de Passe', widget=forms.PasswordInput)
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
        ]

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Un Utilisateur avec ce Nom d'Utilisateur Existe deja")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Un Utilisateur avec cet Email Existe deja")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Les Deux Mots ne concordes pas Verifier")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


class UserEditForm(forms.ModelForm):
    class Meta :
        model = User
        fields = [
            'first_name',
            'last_name',
        ]


class ProfileEdit(forms.ModelForm):
    date_naiss = forms.DateField(
        widget=DatePicker(options={"format": "dd/mm/yyyy", "autoclose": True}))

    class Meta:
        model = Profile
        fields = [
            'date_naiss',
            'pays',
            'ville',
            'contact',
            'facebook',
            'twitter',
            'linkedin',
            'sexe',
            'emploie',
            'image',
            'bio',
        ]
