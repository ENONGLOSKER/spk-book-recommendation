# Generated by Django 5.0.3 on 2024-05-02 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spk_perpus_app', '0004_alter_kriteria_bobot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Penilaian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternatif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spk_perpus_app.alternatif')),
                ('kriteria1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kriteria1', to='spk_perpus_app.crips')),
                ('kriteria2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kriteria2', to='spk_perpus_app.crips')),
                ('kriteria3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kriteria3', to='spk_perpus_app.crips')),
                ('kriteria4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kriteria4', to='spk_perpus_app.crips')),
            ],
        ),
    ]
