# Generated by Django 4.2.14 on 2024-08-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_condicionesimport'),
    ]

    operations = [
        migrations.AddField(
            model_name='importarasistenciadetalle',
            name='linea',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
