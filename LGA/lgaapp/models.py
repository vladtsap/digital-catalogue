from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    # reeeeeeeeeeeeeeeeeeeeeeeeeeeeee

    class Meta:
        ordering = ['name']
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'

    def __str__(self):
        return self.name


class Art(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Мистецтво'
        verbose_name_plural = 'Мистецтво'

    def __str__(self):
        return str(self.name)


class Group(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    art = models.ForeignKey(Art, related_name='books', verbose_name='Мистецтво', on_delete=models.CASCADE, default=None)

    class Meta:
        ordering = ['name']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name
