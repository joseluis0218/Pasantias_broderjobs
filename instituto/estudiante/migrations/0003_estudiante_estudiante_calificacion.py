# Generated by Django 2.1.5 on 2019-02-19 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0002_remove_estudiante_calificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='estudiante_calificacion',
            field=models.CharField(blank=True, choices=[('SC', 'Sin Calificar'), ('B', 'Bueno'), ('MB', 'Muy Bueno'), ('R', 'Regular')], default='SC', max_length=2, null=True),
        ),
    ]