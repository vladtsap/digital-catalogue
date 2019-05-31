from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from django import forms

from .models import Book, Search

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
        Field('name', autocomplete='off', required=True),
        Field('author', autocomplete='off', required=True),
        Field('publication', autocomplete='off'),
        Field('description', autocomplete='off'),
        Field('series', autocomplete='off'),
        Field('personality', autocomplete='off'),
        Field('additional', rows=3),
        Field('isbn', autocomplete='off'),
        Field('inventory_number', autocomplete='off', required=True),
        Field('cipher', autocomplete='off'),
        Field('year', autocomplete='off'),
        Field('place', autocomplete='on'),
        Field('language', autocomplete='on'),
        Field('country', autocomplete='on'),
        Field('subject', css_class='custom-select d-block w-100'),
        Field('art', css_class='custom-select d-block w-100'),
        Field('group', css_class='custom-select d-block w-100'),
        Field('slug', type='hidden'),
        Div(
            Div(
                Submit('update', 'Готово', css_class="btn btn-primary btn-lg btn-block"),
                css_class='offset-sm-1 col-sm-4'
            ),
            css_class='form-group row'
        )
    )

class SearchBook(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('n',
                  'a',
                  'publ',
                  'ser',
                  'pers',
                  'isbn',
                  'invnum',
                  'ciph',
                  'yfr',
                  'yto',
                  'plc',
                  'lang',
                  'cntr',
                  'subj',
                  'art',
                  'gr',)

    helper = FormHelper()
    helper.form_method = 'GET'
    helper.form_action = '/search/result/'
    helper.label_class = 'col-md-6'
    helper.field_class = 'col-md-6'
    helper.layout = Layout(
        Field('n', autocomplete='off'),
        Field('a', autocomplete='off'),
        Field('publ', autocomplete='off'),
        Field('ser', autocomplete='off'),
        Field('pers', autocomplete='off'),
        Field('isbn', autocomplete='off'),
        Field('invnum', autocomplete='off'),
        Field('ciph', autocomplete='off'),
        Field('yfr', autocomplete='off', css_class='col-md-3'),
        Field('yto', autocomplete='off'),
        Field('plc', autocomplete='on'),
        Field('lang', autocomplete='on'),
        Field('cntr', autocomplete='on'),
        Field('subj', css_class='custom-select d-block w-100'),
        Field('art', css_class='custom-select d-block w-100'),
        Field('gr', css_class='custom-select d-block w-100'),
        Div(
            Div(
                Submit('search', 'Пошук', css_class="btn btn-primary btn-lg btn-block"),
                css_class='offset-sm-1 col-sm-4'
            ),
            css_class='form-group row'
        )
    )