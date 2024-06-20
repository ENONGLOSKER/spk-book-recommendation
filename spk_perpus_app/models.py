from django.db import models

# Create your models here.

"""
class Alternatif:
    merupakan tabel dari alternatif, yang memiliki kolom sebagai berikut:
    - simbol, dengan tipe data teks(varchar/charfield) degan panjang maksimal 10 digit 
    - nama, memiliki tipe data yang sama namun panjang maksimalnya 50 digit
    - created,  dengan tipe data tanggal dan waktu (datetime) yang secara otomatis terisi berdasarkan waktu data alternatif dibuat(auto_now_add=True)
    - updated,  dengan tipe yang sama dengan created namun akan terisi saat data alternatif di perbarui/edit(auto_now=True)
"""
class Alternatif(models.Model):
    simbol = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.simbol

"""
class Kriteria:
    merupakan tabel dari Kriteria, yang memiliki kolom sebagai berikut:
    - nama, dengan tipe data teks(varchar/charfield) degan panjang maksimal 50 digit 
    - bobot, dengan tipe data bilangan desimal atau bilangan berkoma(FloatField)
    - atribut, dengan tipe data teks(varchar/charfield) degan panjang maksimal 50 digit 
    - created,  dengan tipe data tanggal dan waktu (datetime) yang secara otomatis terisi berdasarkan waktu data alternatif dibuat(auto_now_add=True)
    - updated,  dengan tipe yang sama dengan created namun akan terisi saat data alternatif di perbarui/edit(auto_now=True)
"""
class Kriteria(models.Model):
    nama = models.CharField(max_length=50)
    bobot = models.FloatField()
    atribut = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nama

"""
class Penilaian:
    merupakan tabel dari Penilaian, yang memiliki kolom sebagai berikut:
    - alternatif, yang berelasi dengan tabel alternatif
    - kriteria1, dengan tipe data bilangan desimal atau bilangan berkoma(FloatField) yang secara otomatis akan berisi dengan nilai 0(nilai default)
    - kriteria2, sama dengan kriteria1
    - kriteria3, sama dengan kriteria1
    - kriteria4, sama dengan kriteria1
"""
class Penilaian(models.Model):
    alternatif = models.ForeignKey(Alternatif, on_delete=models.CASCADE )
    kriteria1 = models.FloatField(default=0)
    kriteria2 = models.FloatField(default=0)
    kriteria3 = models.FloatField(default=0)
    kriteria4 = models.FloatField(default=0)

"""
class Normalisasi dan Rengking:
    merupakan tabel dari Penilaian, yang memiliki kolom sama seperti dengan tabel penilaian namun tidak memiliki nilai default(ada atau tidaknya tidak berpengaruh karena optional sebagai antisipasi user tidak mengisi nilai saja)

    - Tujauannya dibuat kedua tabel tersebut adalah untuk mempermudah dalam pengeloloaan operasi perhitungan atau sebagai tabel pembantu
"""
class Normalisasi(models.Model):
    alternatif = models.ForeignKey(Alternatif, on_delete=models.CASCADE )
    kriteria1 = models.FloatField()
    kriteria2 = models.FloatField()
    kriteria3 = models.FloatField()
    kriteria4 = models.FloatField()

class Rengking(models.Model):
    alternatif = models.ForeignKey(Alternatif, on_delete=models.CASCADE )
    kriteria1 = models.FloatField()
    kriteria2 = models.FloatField()
    kriteria3 = models.FloatField()
    kriteria4 = models.FloatField()
    total_nilai = models.FloatField()
