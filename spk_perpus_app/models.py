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
    bobot = models.IntegerField()
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
