# Generated by Django 3.0.8 on 2020-10-29 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remedio', '0007_auto_20201029_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recomendacao',
            name='horarios',
        ),
    ]