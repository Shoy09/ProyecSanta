# Generated by Django 4.0 on 2024-07-05 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_externos_id_general'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externos',
            name='dni',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]