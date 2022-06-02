from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div
from django import forms

from lgaapp.models import Book


class AddBook(forms.ModelForm):
	class Meta:
		model = Book
		fields = (
			'name',
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
		Field('author', autocomplete='off'),
		Field('name', autocomplete='off', required=True),
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
