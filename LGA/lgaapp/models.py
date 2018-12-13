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
