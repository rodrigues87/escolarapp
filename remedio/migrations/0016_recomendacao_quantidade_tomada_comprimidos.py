# Generated by Django 3.0.8 on 2020-11-19 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remedio', '0015_auto_20201118_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='recomendacao',
            name='quantidade_tomada_comprimidos',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
