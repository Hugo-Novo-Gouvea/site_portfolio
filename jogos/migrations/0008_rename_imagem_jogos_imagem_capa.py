# Generated by Django 5.0 on 2023-12-16 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0007_remove_jogos_nome_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jogos',
            old_name='imagem',
            new_name='imagem_capa',
        ),
    ]
