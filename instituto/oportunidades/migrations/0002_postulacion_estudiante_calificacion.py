# Generated by Django 2.1.5 on 2019-02-18 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulacion',
            name='estudiante_calificacion',
            field=models.CharField(blank=True, choices=[('SC', 'Sin Calificar'), ('B', 'Bueno'), ('MB', 'Muy Bueno'), ('R', 'Regular')], default='SC', max_length=2, null=True),
        ),
    ]
