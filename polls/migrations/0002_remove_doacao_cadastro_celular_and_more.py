# Generated by Django 5.0.3 on 2024-05-13 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doacao_cadastro',
            name='Celular',
        ),
        migrations.RemoveField(
            model_name='doacao_cadastro',
            name='Data_da_Doacao',
        ),
        migrations.RemoveField(
            model_name='doacao_cadastro',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='doacao_cadastro',
            name='Itens_da_Doacao',
        ),
    ]
