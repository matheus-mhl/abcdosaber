# Generated by Django 4.2.18 on 2025-02-10 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrutores',
            fields=[
                ('codigo', models.IntegerField(help_text='Código do Instrutores', primary_key=True, serialize=False)),
                ('descricao', models.CharField(help_text='Informe a descrição do Instrutores', max_length=100)),
            ],
        ),
    ]
