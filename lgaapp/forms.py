from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div
from django import forms

from .models import Book, Search


class AddBook(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('name',
				  'author',
				  'publication',
				  'additional',
				  'description',
				  'series',
				  'personality',
				  'isbn',
				  'inventory_number',
				  'cipher',
				  'year',
				  'place',
				  'language',
				  'subject',
				  'art',
				  'country',
				  'group',
				  )

	helper = FormHelper()
	helper.form_method = 'POST'
	helper.label_class = 'col-md-6'
	helper.field_class = 'col-md-6'
	helper.layout = Layout(
		Field('name', autocomplete='off', required=True),
		Field('author', autocomplete='off'),
		Field('publication', autocomplete='off'),
		Field('additional', autocomplete='off'),
		Field('description', autocomplete='off'),
		Field('series', autocomplete='off'),
		Field('personality', autocomplete='off'),
		Field('isbn', autocomplete='off'),
		Field('inventory_number', autocomplete='off'),
		Field('cipher', autocomplete='off'),
		Field('year', autocomplete='off'),
		Field('place', css_class='custom-select d-block w-100'),
		Field('language', autocomplete='off'),
		Field('subject', css_class='custom-select d-block w-100'),
		Field('art', css_class='custom-select d-block w-100'),
		Field('country', autocomplete='off'),
		Field('group', css_class='custom-select d-block w-100'),
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
				  'add',
				  'ser',
				  'pers',
				  'invnum',
				  'yfr',
				  'yto',
				  'plc',
				  'lang',
				  'subj',
				  'art',
				  'cntr',
				  'gr',)

	helper = FormHelper()
	helper.form_method = 'GET'
	helper.form_action = '/search/result/'
	helper.layout = Layout(
		Field('n', autocomplete='off'),
		Field('a', autocomplete='off'),
		Field('publ', autocomplete='off'),
		Field('add', autocomplete='off'),
		Field('ser', autocomplete='off'),
		Field('pers', autocomplete='off'),
		Field('invnum', autocomplete='off'),
		Field('yfr', autocomplete='off'),
		Field('yto', autocomplete='off'),
		Field('plc', css_class='custom-select d-block w-100'),
		Field('lang', autocomplete='off'),
		Field('subj', css_class='custom-select d-block w-100'),
		Field('art', css_class='custom-select d-block w-100'),
		Field('cntr', autocomplete='off'),
		Field('gr', css_class='custom-select d-block w-100'),
		Div(
			Div(
				Submit('search', 'Пошук', css_class="btn btn-primary btn-lg btn-block"),
				css_class='offset-sm-1 col-sm-4'
			),
			css_class='form-group row'
		)
	)
