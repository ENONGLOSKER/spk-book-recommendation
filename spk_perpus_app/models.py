from django.db import models

# Create your models here.
class Alternatif(models.Model):
    simbol = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.simbol
    
class Kriteria(models.Model):
    nama = models.CharField(max_length=50)
    bobot = models.FloatField()
    atribut = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nama
    
class Crips(models.Model):
    kriteria = models.ForeignKey(Kriteria, on_delete=models.CASCADE, related_name='crips' )
    keterangan = models.CharField(max_length=100)
    nilai = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.nilai)


class Penilaian(models.Model):
    alternatif = models.ForeignKey(Alternatif, on_delete=models.CASCADE )
    kriteria1 = models.ForeignKey(Crips, related_name='kriteria1', on_delete=models.CASCADE)
    kriteria2 = models.ForeignKey(Crips, related_name='kriteria2', on_delete=models.CASCADE)
    kriteria3 = models.ForeignKey(Crips, related_name='kriteria3', on_delete=models.CASCADE)
    kriteria4 = models.ForeignKey(Crips, related_name='kriteria4', on_delete=models.CASCADE)

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
