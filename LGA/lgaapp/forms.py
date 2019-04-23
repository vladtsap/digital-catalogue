from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from django import forms

from .models import Book


class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name',
                  'author',
                  'publication',
                  'description',
                  'series',
                  'personality',
                  'additional',
                  'isbn',
                  'inventory_number',
                  'cipher',
                  'year',
                  'place',
                  'language',
                  'country',
                  'subject',
                  'art',
                  'group',
                  'slug',)


    helper = FormHelper()
    helper.form_method = 'POST'
    helper.label_class = 'col-md-6'
    helper.field_class = 'col-md-6'
    helper.layout = Layout(
        Field('name', autocomplete='off'),
        Field('author', autocomplete='off'),
        Field('publication', autocomplete='off'),
        Field('description', autocomplete='off'),
        Field('series', autocomplete='off'),
        Field('personality', autocomplete='off'),
        Field('additional', rows=3),
        Field('isbn', autocomplete='off'),
        Field('inventory_number', autocomplete='off'),
        Field('cipher', autocomplete='off'),
        Field('year', autocomplete='off'),
        Field('place', autocomplete='on'),
        Field('language', autocomplete='on'),
        Field('country', autocomplete='on'),
        Field('subject', css_class='custom-select d-block w-100'),
        Field('art', css_class='custom-select d-block w-100'),
        Field('group', css_class='custom-select d-block w-100'),
        Field('slug', type='hidden'),
        FormActions(Submit('update', 'Готово', css_class='btn btn-primary btn-lg btn-block'))
    )
