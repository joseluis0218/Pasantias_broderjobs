# Generated by Django 2.1.5 on 2019-03-15 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190302_0121'),
        ('oportunidades', '0005_auto_20190304_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidad',
            name='distrito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Distrito'),
        ),
    ]
