# Generated by Django 5.0.3 on 2024-05-02 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spk_perpus_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('bobot', models.IntegerField()),
                ('atribut', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
