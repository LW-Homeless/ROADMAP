from django import forms
from .models import Article

from django_ckeditor_5.widgets import CKEditor5Widget


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article

        fields = ['title', 'publishing_date', 'description', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'publishing_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control form-control-sm'}),
            'description': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'content': CKEditor5Widget(attrs={'class': 'django_ckeditor_5'})
        }
