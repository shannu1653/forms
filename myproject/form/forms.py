from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from django.core.exceptions import ValidationError
import datetime

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Date of Birth')
    mobile = forms.CharField(max_length=15, label='Mobile Number')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already in use.")
        return email

    def clean_password2(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError("Passwords do not match.")
        return p2

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob and dob > datetime.date.today():
            raise ValidationError("DOB cannot be in the future.")
        return dob
