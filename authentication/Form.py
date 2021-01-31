from django.contrib.auth.models import User;
from django.core.validators import EmailValidator, ValidationError
from django import forms


class Signupform(forms.ModelForm):
    class Meta:
        model=User;
        fields=["email",'username','password'];


    def clean_email(self):
        email = self.cleaned_data['email'];
        if not email and not email.endswith('@'):
            raise forms.ValidationError('Enter the email!.');
        elif User.objects.filter(email=email).first():
            raise forms.ValidationError('Email is already taken Register.')
        return email
        
    

            

        
        
