# Generated by Django 2.2.3 on 2019-07-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hewan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('spesies', models.CharField(max_length=255)),
                ('berat', models.FloatField()),
                ('umur', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kandang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('isi_kandang', models.TextField()),
                ('luas_kandang', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pengunjung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nomor_telepon', models.CharField(max_length=20)),
                ('hari_berkunjung', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Penjaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nomor_telepon', models.CharField(max_length=20)),
                ('jadwal_jaga', models.TimeField()),
            ],
        ),
    ]
