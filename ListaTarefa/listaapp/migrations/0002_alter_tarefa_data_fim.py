# Generated by Django 5.0.1 on 2024-01-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='data_fim',
            field=models.DateField(blank=True, null=True),
        ),
    ]
