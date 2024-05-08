# Generated by Django 5.0.3 on 2024-05-03 01:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spk_perpus_app', '0005_penilaian'),
    ]

    operations = [
        migrations.CreateModel(
            name='Normalisasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kriteria1', models.FloatField()),
                ('kriteria2', models.FloatField()),
                ('kriteria3', models.FloatField()),
                ('kriteria4', models.FloatField()),
                ('alternatif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spk_perpus_app.alternatif')),
            ],
        ),
    ]