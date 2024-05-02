from django import forms
from .models import Alternatif, Kriteria, Crips


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