from django import forms
from .models import Alternatif, Kriteria, Penilaian


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

# class CripsForm(forms.ModelForm):
#     class Meta:
#         model = Crips
#         fields = "__all__"

#         widgets = {
#             'kriteria':forms.Select(attrs={'class':'form-control'}),
#             'keterangan':forms.TextInput(attrs={'class':'form-control'}),
#             'nilai':forms.NumberInput(attrs={'class':'form-control'}),
#         }

class PenilaianForm(forms.ModelForm):
    
    class Meta:
        model = Penilaian
        fields = "__all__"

        widgets = {
            'alternatif':forms.Select(attrs={'class':'form-control'}),
            'kriteria1':forms.NumberInput(attrs={'class':'form-control'}),
            'kriteria2':forms.NumberInput(attrs={'class':'form-control'}),
            'kriteria3':forms.NumberInput(attrs={'class':'form-control'}),
            'kriteria4':forms.NumberInput(attrs={'class':'form-control'}),
        }