from django import forms
from home.models import Contact,Newsletter
from django.forms import ModelForm

from .models import *


class ContactForm(forms.ModelForm):
    phone  = forms.DecimalField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your phone number here...'
        }
    ))
    class Meta:
        model = Contact

        fields = [
            'name',
            'email',
            'content'
            
        ]


class NewsletterForm(forms.ModelForm):

    attrs={
        'class':'form-control',
        'placeholder': 'Write your email here...'
    }
    class Meta:
        model = Newsletter
        fields = [
            'email'
       ]