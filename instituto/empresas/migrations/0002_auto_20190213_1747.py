# Generated by Django 2.1.5 on 2019-02-13 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='fecha_activacion',
        ),
        migrations.RemoveField(
            model_name='representante',
            name='fecha_activacion',
        ),
    ]
