# Generated by Django 2.1.5 on 2019-02-19 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0004_auto_20190219_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='calificacion',
        ),
    ]