from django import forms
from .models import Alternatif, Kriteria, Crips, Penilaian


class AlternatifForm(forms.ModelForm):
    class Meta:
        model = Alternatif
        fields = "__all__"

        widgets = {
            'simbol':forms.TextInput(attrs={'class':'form-control'}),
            'nama':forms.TextInput(attrs={'class':'form-control'}),
        }

class KriteriaForm(forms.ModelForm):
    class Meta:
        model = Kriteria
        fields = "__all__"

        widgets = {
            'nama':forms.TextInput(attrs={'class':'form-control'}),
            'bobot':forms.NumberInput(attrs={'class':'form-control'}),
            'atribut':forms.TextInput(attrs={'class':'form-control'}),
        }

class CripsForm(forms.ModelForm):
    class Meta:
        model = Crips
        fields = "__all__"

        widgets = {
            'kriteria':forms.Select(attrs={'class':'form-control'}),
            'keterangan':forms.TextInput(attrs={'class':'form-control'}),
            'nilai':forms.NumberInput(attrs={'class':'form-control'}),
        }

class PenilaianForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PenilaianForm, self).__init__(*args, **kwargs)

        # Mendapatkan semua kriteria
        all_kriteria = Kriteria.objects.all()

        # Melakukan iterasi untuk setiap kriteria
        for i in range(4):
            field_name = f'kriteria{i+1}'
            field = self.fields[field_name]

            # Mendapatkan objek kriteria ke-i
            kriteria = all_kriteria[i] if i < len(all_kriteria) else None

            if kriteria:
                # Mengisi pilihan (choices) dengan keterangan crips dan nilainya
                choices = [(crips.id, f"{kriteria.nama} | {crips.keterangan} | {crips.nilai}") for crips in kriteria.crips.all()]
                field.choices = choices
            else:
                # Jika tidak ada kriteria, kosongkan pilihan
                field.choices = [("", "")]
                
    class Meta:
        model = Penilaian
        fields = "__all__"

        widgets = {
            'alternatif':forms.Select(attrs={'class':'form-control'}),
            'kriteria1':forms.Select(attrs={'class':'form-control'}),
            'kriteria2':forms.Select(attrs={'class':'form-control'}),
            'kriteria3':forms.Select(attrs={'class':'form-control'}),
            'kriteria4':forms.Select(attrs={'class':'form-control'}),
          
        }