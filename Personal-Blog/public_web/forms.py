from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_mail', 'contact_subject', 'contact_message']

        widgets = {
            'contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'contact_mail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'contact_subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'contact_message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'})
        }
