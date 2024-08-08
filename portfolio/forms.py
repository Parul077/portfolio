# portfolio/forms.py

from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'John'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Doe'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'you@domain.com'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your message here ...'}))
