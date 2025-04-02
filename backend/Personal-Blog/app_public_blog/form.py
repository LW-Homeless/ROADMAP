from django import forms
from .models import Article, Contact

from django_ckeditor_5.widgets import CKEditor5Widget


class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['article_content'].required = False

    class Meta:
        model = Article
        fields = ['article_title', 'article_date', 'article_description', 'article_content']

        widgets = {
            'article_title': forms.TextInput(attrs={'class': 'form-control', 'id': 'txtTitle'}),
            'article_date': forms.DateTimeInput(attrs={'class': 'form-control',
                                                       'id': 'txtDate',
                                                       'type': 'datetime-local'}),
            'article_description': forms.TextInput(attrs={'class': 'form-control', 'id': 'txtDescription'}),
            'article_content': CKEditor5Widget(attrs={'class': 'django_ckeditor_5'}, config_name='extends')
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_email', 'contact_suject', 'contact_message']

        widgets = {
            'contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'contact_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'contact_suject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'contact_message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'})
        }


class CustomAuthForm(forms.Form):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'class':  'form-control'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
