from django import forms
from .models import User
"""class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'birth_date','phone_number', 'email']

class SignupForm(forms.Form):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']"""