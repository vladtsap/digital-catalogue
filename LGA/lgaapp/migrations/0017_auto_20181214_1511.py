# Generated by Django 2.1.4 on 2018-12-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lgaapp', '0016_remove_book_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='object',
        ),
        migrations.AlterField(
            model_name='book',
            name='place',
            field=models.CharField(blank=True, max_length=200, verbose_name='Місцезнаходження'),
        ),
    ]