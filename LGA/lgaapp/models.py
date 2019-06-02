from django.db import models


# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

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
    name = models.CharField(max_length=200, db_index=True, verbose_name="Назва", default=None, blank=True)
    author = models.CharField(max_length=200, verbose_name="Автор", default=None, blank=True)
    publication = models.CharField(max_length=200, db_index=True, verbose_name="Видання", default=None, blank=True)
    description = models.TextField(verbose_name="Опис", blank=True)
    series = models.PositiveIntegerField(verbose_name="Серія", null=True, blank=True)
    personality = models.CharField(max_length=200, db_index=True, verbose_name="Персоналії", default=None, blank=True)
    additional = models.CharField(max_length=200, db_index=True, verbose_name="Додатково", default=None, blank=True)
    isbn = models.CharField(max_length=20, verbose_name="ISBN", default=None, blank=True)
    inventory_number = models.CharField(max_length=200, verbose_name="Інвентарний номер", default=None, blank=True)
    cipher = models.CharField(max_length=200, verbose_name="Шифр книги", default=None, blank=True)
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
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name


class Search(models.Model):
    n = models.CharField(max_length=200, verbose_name="Назва", blank=True)
    a = models.CharField(max_length=200, verbose_name="Автор", default=None, blank=True)
    publ = models.CharField(max_length=200, verbose_name="Місце видання", default=None, blank=True)
    ser = models.PositiveIntegerField(verbose_name="Серія", blank=True)
    pers = models.CharField(max_length=200, verbose_name="Персоналії", blank=True)
    isbn = models.CharField(max_length=200, verbose_name="ISBN", blank=True)
    invnum = models.CharField(max_length=200, verbose_name="Інвентарний номер", blank=True)
    ciph = models.CharField(max_length=200, verbose_name="Шифр книги", blank=True)
    yfr = models.CharField(max_length=200, verbose_name="З року", blank=True)
    yto = models.CharField(max_length=200, verbose_name="До року", blank=True)
    plc = models.CharField(max_length=200, verbose_name="Місцезнаходження", default=None, null=True, blank=True)
    lang = models.CharField(max_length=200, verbose_name="Мова", blank=True)
    cntr = models.CharField(max_length=200, verbose_name="Країна", blank=True)
    subj = models.ForeignKey(Subject, max_length=200, verbose_name="Тематика", default=None, on_delete=models.CASCADE, null=True, blank=True)
    art = models.ForeignKey(Art, max_length=200, verbose_name="Мистецтво", default=None, on_delete=models.CASCADE, null=True, blank=True)
    gr = models.ForeignKey(Group, max_length=200, verbose_name="Групи", default=None, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name
