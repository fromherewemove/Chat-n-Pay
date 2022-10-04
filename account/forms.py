from django import forms
from django.forms.widgets import *
from .models import CustomUser

class UserRegistration(forms.ModelForm):
    password1 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'Type in your password', 'required':'required'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'Confrim Password', 'required':'required'}))
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'date_of_birth', 'email')
        widgets = {
            'first_name': TextInput(attrs={'class':'form', 'placeholder':'Your First Name', 'required': 'required'}),
            'last_name': TextInput(attrs={'class':'form', 'placeholder':'Your Last Name', 'required': 'required'}),
            'date_of_birth': DateInput(attrs={'class':'form', 'placeholder':'The Day you were born', 'required': 'required', 'type': 'date'}),
            'email': EmailInput(attrs={'class':'form', 'placeholder':'Your EmailAddress', 'required':'required'})        

        }
    def get_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords arent the same")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class CustomAuthForm(forms.Form): 
    email = forms.CharField(widget=EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'required':'required'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class':'form-control','placeholder':'Password', 'required':'required'}))