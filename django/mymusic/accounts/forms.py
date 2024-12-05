from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label='Подтвердите пароль')

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают.")


class UserPasswordChangeForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ('password',)