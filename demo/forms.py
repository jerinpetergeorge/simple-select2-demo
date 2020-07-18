from django import forms
from django.forms import DateInput
from simple_select2 import AutoCompleteSelect2Multiple, AutoCompleteSelect2
from .models import Article


class _NativeDatePickerWidget(DateInput):
    input_type = 'date'


class Select2ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'publications': AutoCompleteSelect2Multiple(url='select2-publication-list'),
            'reporter': AutoCompleteSelect2(url='select2-reporter-list'),
            'pub_date': _NativeDatePickerWidget,
        }
