from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.forms.widgets import NumberInput
from .models import User
from .validators import age_validator
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm


class AccountRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Lastname'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}), )
    password2 = forms.CharField(label='Confirm Password', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}), )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class AccountLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'required': True, 'autofocus': True}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'required': True}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'placeholder': 'Password', 'required': False}))


class AccountPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(AccountPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'type': 'email',
        'name': 'email'
    }))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = "There is no user registered with the specified E-Mail address."
            self.add_error('email', msg)
        return email
