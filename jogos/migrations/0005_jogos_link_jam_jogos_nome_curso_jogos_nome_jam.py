# Generated by Django 5.0 on 2023-12-16 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0004_rename_data_jogo_certificados_data_certificado'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogos',
            name='link_jam',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='jogos',
            name='nome_curso',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='jogos',
            name='nome_jam',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
