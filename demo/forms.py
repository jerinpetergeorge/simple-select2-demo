from django import forms
from simple_select2 import AutoCompleteSelect2Multiple, AutoCompleteSelect2
from .models import Article


class Select2ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'publications': AutoCompleteSelect2Multiple(url='select2-publication-list'),
            'reporter': AutoCompleteSelect2(url='select2-reporter-list')
        }
