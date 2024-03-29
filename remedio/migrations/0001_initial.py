# Generated by Django 3.0.8 on 2020-11-19 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Remedio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('mg', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name_plural': 'Remedios',
            },
        ),
        migrations.CreateModel(
            name='Recomendacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intervalo', models.IntegerField()),
                ('dias', models.IntegerField()),
                ('ultima_hora_que_tomou', models.DateTimeField(blank=True, null=True)),
                ('quantidade_total_comprimidos', models.IntegerField(blank=True, null=True)),
                ('quantidade_tomada_comprimidos', models.IntegerField(default=0)),
                ('quantidade_restante', models.IntegerField(blank=True, null=True)),
                ('proximo_horario', models.DateTimeField(blank=True, null=True)),
                ('remedio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remedio.Remedio')),
            ],
            options={
                'verbose_name_plural': 'Recomendações',
            },
        ),
    ]
