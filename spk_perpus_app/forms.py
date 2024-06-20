from django import forms
from .models import Alternatif, Kriteria, Penilaian

"""
class AlternatifForm, class KriteriaForm dan class PenilaianForm:

    Kode tersebut mendefinisikan tiga kelas form: [AlternatifForm], [KriteriaForm] dan [PenilaianForm]. Tujuannya adalah untuk membuat form yang terkait dengan model [Alternatif], [Kriteria], dan [Penilaian] agar dapat diinputkan oleh pengguna melalui halaman web nya.

    - Setiap kelas form menggunakan model form dari Django (`forms.ModelForm`) yang memudahkan pembuatan form berdasarkan model yang terkait. 
    - Dalam setiap kelas form, [Meta] class digunakan untuk menghubungkan form dengan model yang sesuai. 
    - Selain itu, penggunaan `fields = "__all__"` memungkinkan form untuk mencakup semua field yang ada dalam model.
    
    Selain itu, setiap form juga mendefinisikan `widgets` yang menentukan tampilan widget untuk setiap field dalam form. Misalnya, `forms.TextInput(attrs={'class':'form-control'})` digunakan untuk menambahkan kelas CSS `form-control` ke input field dalam form untuk memperindah tampilan antarmuka pengguna.
"""
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