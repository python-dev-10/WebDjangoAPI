# Generated by Django 3.2 on 2021-06-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_diarista_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='diarista',
            name='cidade',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
