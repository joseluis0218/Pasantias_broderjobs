# Generated by Django 2.1.5 on 2019-02-23 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0005_remove_empresa_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d', verbose_name='logo'),
        ),
    ]
