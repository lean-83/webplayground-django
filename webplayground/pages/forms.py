from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Título'}),
            'content': forms.Textarea(attrs={'class': 'form_control'}),
            'order': forms.NumberInput(attrs={'class': 'form_control'}),
        }
        labels = {
            'title': '', 'content': '', 'order': ''
        }