from django.db import models

# Create your models here.
class Subject(models.Model):
	name = models.CharField(max_length=200, db_index=True, unique=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)
	#reeeeeeeeeeeeeeeeeeeeeeeeeeeeee


	class Meta:
		ordering = ['name']
		verbose_name = 'Тематика'
		verbose_name_plural = 'Тематики'

	def __str__(self):
		return self.name


class Art(models.Model):
	name = models.CharField(max_length=200, db_index=True, unique=True)
	country = models.CharField(max_length=200, db_index=True, unique=True)

	class Meta:
		ordering = ['country']
		verbose_name = 'Мистецтво'
		verbose_name_plural = 'Мистецтво'

	def __str__(self):
		return str(self.name) + str(self.country)

class Group(models.Model):
	GROUP_CHOICES = (
		(u'VI', u'Вітчизняні'),
		(u'IN', u'Іноземні'),
		(u'PI', u'Періодика'),
		(u'CA', u'Каталог'),
	)
	name = models.CharField(max_length=200, choices=GROUP_CHOICES, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)

	class Meta:
		ordering = ['name']
		verbose_name = 'Групи'
		verbose_name_plural = 'Групи'

	def __str__(self):
		return self.name