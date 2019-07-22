from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length=255)
    spesies = models.CharField(max_length=255)
    berat = models.FloatField()
    umur = models.IntegerField()

class Kandang(models.Model):
    nama = models.CharField(max_length=255)
    isi_kandang = models.TextField()
    luas_kandang = models.FloatField()

class Penjaga(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=20)
    jadwal_jaga = models.TimeField()

class Pengunjung(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=20)
    hari_berkunjung = models.DateField()
