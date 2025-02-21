# Generated by Django 4.2.18 on 2025-02-12 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turmas',
            fields=[
                ('numero', models.BigAutoField(primary_key=True, serialize=False)),
                ('horarioAula', models.TimeField(blank=True, max_length=70, null=True)),
                ('duraçaoAula', models.DurationField(null=True)),
                ('data_inicial', models.DateField(null=True)),
                ('dataFinal', models.DateField(null=True)),
            ],
        ),
    ]
