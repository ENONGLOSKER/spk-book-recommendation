# Generated by Django 5.0.3 on 2024-05-02 03:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spk_perpus_app', '0002_kriteria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keterangan', models.CharField(max_length=100)),
                ('nilai', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('kriteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crips', to='spk_perpus_app.kriteria')),
            ],
        ),
    ]
