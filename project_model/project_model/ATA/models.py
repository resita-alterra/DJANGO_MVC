from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    no_telepon = models.CharField(max_length=20)
    jabatan = models.CharField(max_length=100)

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    no_telepon = models.CharField(max_length=20)
    no_absen = models.IntegerField()
    nilai_rata_rata = models.FloatField()

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=100)
    jadwal_dimulai = models.DateTimeField()
    jadwal_berakhir = models.DateTimeField()
    
class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    no_telepon = models.CharField(max_length=20)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=100)
    banyak_soal = models.IntegerField()
    bobot_nilai = models.IntegerField()
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length=100)
    banyak_soal = models.IntegerField()
    bobot_nilai = models.IntegerField()
    tanggal_pelaksanaan = models.DateField()
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)


