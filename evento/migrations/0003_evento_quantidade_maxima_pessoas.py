# Generated by Django 3.0.8 on 2020-12-04 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0002_favorito_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='quantidade_maxima_pessoas',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
