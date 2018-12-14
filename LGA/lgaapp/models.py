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
        verbose_name = 'Групи'
        verbose_name_plural = 'Групи'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Назва", default=None)
    author = models.CharField(max_length=200, db_index=True, verbose_name="Автор", default=None)
    publication = models.CharField(max_length=200, db_index=True, verbose_name="Видання", default=None, blank=True)
    description = models.TextField(verbose_name="Опис", blank=True)
    series = models.PositiveIntegerField(verbose_name="Серія", null=True, blank=True)
    personality = models.CharField(max_length=200, db_index=True, verbose_name="Персоналії", default=None, blank=True)
    additional = models.CharField(max_length=200, db_index=True, verbose_name="Додатково", default=None, blank=True)
    isbn = models.CharField(max_length=20, verbose_name="ISBN", default=None)
    inventory_number = models.IntegerField(verbose_name="Інвентарний номер", default=None)
    cipher = models.PositiveIntegerField(verbose_name="Шифр книги", default=None)
    year = models.CharField(max_length=200, verbose_name="Рік видання", default=None, blank=True)
    place = models.CharField(max_length=200, verbose_name="Місцезнаходження", default=None, blank=True)
    language = models.CharField(max_length=200, db_index=True, verbose_name="Мова",default=None, blank=True)
    country = models.CharField(max_length=200, db_index=True, verbose_name="Країна", default=None, blank=True)
    subject = models.ForeignKey(Subject, max_length=200, verbose_name="Тематика", default=None, on_delete=models.CASCADE, null=True, blank=True)
    art = models.ForeignKey(Art, max_length=200, verbose_name="Мистецтво", default=None, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(Group, max_length=200, verbose_name="Групи", default=None, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Книги'
        verbose_name_plural = 'Книга'

    def __str__(self):
        return self.name