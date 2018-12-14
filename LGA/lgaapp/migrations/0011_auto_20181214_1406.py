# Generated by Django 2.1.4 on 2018-12-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lgaapp', '0010_auto_20181214_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cipher',
            field=models.IntegerField(default=None, verbose_name='Шифр книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='inventory_number',
            field=models.IntegerField(default=None, verbose_name='Інвентарний номер'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(default=None, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.IntegerField(default=None, verbose_name='Серія'),
        ),
    ]