# Generated by Django 4.2.18 on 2025-02-11 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('titulos', '0001_initial'),
        ('instrutores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrutores',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='instrutores',
            name='descricao',
        ),
        migrations.AddField(
            model_name='instrutores',
            name='codigo_titulos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='titulos.titulos'),
        ),
        migrations.AddField(
            model_name='instrutores',
            name='data_nascimento',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='instrutores',
            name='ddd',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='instrutores',
            name='id',
            field=models.BigAutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instrutores',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='instrutores',
            name='rg',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instrutores',
            name='telefone',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
