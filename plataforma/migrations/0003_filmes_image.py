# Generated by Django 4.0.3 on 2022-03-27 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0002_assinatura_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmes',
            name='image',
            field=models.ImageField(default='', upload_to='media/movies_covers'),
        ),
    ]
