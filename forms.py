from django import forms
from .models import Usersdetails


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usersdetails
        fields = ['username','email','password']
