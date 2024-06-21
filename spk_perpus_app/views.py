from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Count, Q
# modul core
from .models import Alternatif, Kriteria, Penilaian, Normalisasi, Rengking
from .forms import AlternatifForm, KriteriaForm, PenilaianForm
from django.views.decorators.cache import cache_page

# Create your views here.
"""
def index : 
    fungsi untuk halaman home, yang hanya memamggil template home.html

"""
def index(request):
    return render(request, 'index.html')

"""
def dashboard : 
    fungsi untuk halaman dashboard, yang memanggil templates dashboard01.html
    menampilkan jumlah data alternatif, kriteria, bobot, rekomendasi berdasarkan perengkingan
    - rekomendasi di dapat dari total nilai tertinggi dari data hasil  perengkingan, jika ada nilai tertinggi yang sama, maka
    akan dihitung berapa total nilai yang sama tersebut sebagai julah rekomendasi (total_rekomendasi).
"""
@login_required
def dashboard(request):
    # Menggunakan select_related untuk mengurangi jumlah query jika ada hubungan ke model lain
    data_rengking = Rengking.objects.select_related('alternatif').all()

    # Menghitung jumlah alternatif, kriteria, dan penilaian
    alternatif_count = Alternatif.objects.count()
    kriteria_count = Kriteria.objects.count()
    penilaian_count = Penilaian.objects.count() / alternatif_count if alternatif_count > 0 else 0

    # Mengambil nilai maksimal dari total_nilai
    max_total = Rengking.objects.aggregate(max_total=Max('total_nilai'))['max_total']

    # Menghitung jumlah rekomendasi berdasarkan nilai maksimal total_nilai
    total_rekomendasi = Rengking.objects.filter(total_nilai=max_total).count()

    # Mengumpulkan data untuk grafik Highcharts
    categories = [rengking.alternatif.nama for rengking in data_rengking]
    series_data = [rengking.total_nilai for rengking in data_rengking]

    context = {
        'categories': categories,
        'series_data': series_data,
        'alternatif': alternatif_count,
        'kriteria': kriteria_count,
        'penilaian': penilaian_count,
        'total_rekomendasi': total_rekomendasi
    }

    # data_rengking = Rengking.objects.all()
    # alternatif = Alternatif.objects.all().count()
    # kriteria = Kriteria.objects.all().count()
    # penilaian = Penilaian.objects.all().count() / Alternatif.objects.all().count()

    # # Mendapatkan total nilai tertinggi
    # max_total = Rengking.objects.aggregate(Max('total_nilai'))['total_nilai__max']
    # # Mendapatkan jumlah rekomendasi
    # total_rekomendasi = Rengking.objects.filter(total_nilai=max_total).count()

    # # Mengumpulkan data untuk grafik Highcharts
    # categories = []
    # series_data = []

    # for rengking in data_rengking:
    #     categories.append(rengking.alternatif.nama)
    #     series_data.append(rengking.total_nilai)

    # context = {
    #     'categories': categories,
    #     'series_data': series_data,
    #     'alternatif':alternatif,
    #     'kriteria':kriteria,
    #     'penilaian':penilaian,
    #     'total_rekomendasi': total_rekomendasi
    # }

    return render(request, 'dashboard01.html', context)


# ALTERNATIF ---------------------------------------------------------------------
"""
def dashboard_alternatif : 
    fungsi untuk halaman dashboard, yang memanggil templates dashboard02.html dan
    menampilkan semua data alternatif dalam bentuk tabel pada templates. dengan cara,
    - mengambil semua data pada tabel alternatif -> datas = Alternatif.objects.all() 
    - data yang sudah diapatkan kemudian di lempar ke templates melalui context -> context ={ 'datas':datas }, 
    tujuanya supaya bisa menampilkan semua data tersebut pada halaman alternatif
"""
@login_required
@cache_page(60 * 15) 
def dashboard_alternatif(request):
    datas = Alternatif.objects.only('simbol', 'nama', 'created', 'updated')

    context ={
        'datas':datas,
    }
    return render(request, 'dashboard02.html', context)

"""
def tambah_alternatif : 
    fungsi untuk form saat menambah data alternatif, degan cara,
    - jika method saat menekan tombol simpan di form adalah POST maka akan menjalakan blok if
    yang dimana akan mengekcek apakah semua data yang di isikan pada kolom form sudah sesuai denga tipe filed pada databasenya
    jika benar maka akan di simpan setelah itu akan di bawa menuju halaman alternatif untuk melihat semua data pada tabel alternatif.
    jika salah maka akan di bawa ke halaman itu sendiri atau halaman form tersebut (ngerefres ulang)
"""
@login_required
def tambah_alternatif(request):
    if request.method == 'POST':
        form = AlternatifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alternatif')
    else:
        form = AlternatifForm()

    context = {
        'form':form,
    }
    return render(request, 'dashboard_form.html', context)

"""
def edit_alternatif:
    fungsi untuk form saat mengedit data alternatif, degan cara,
    - ambil data mana yang harus di edit tersebut dengan cara mengambil id nya (karena setiap alternatif memiliki id yang berbeda /primeri key)
    - setelah mendapatkan data yang mau diedit maka cek metode request nya jika POST maka akan mengambil data baru yang diisikan pada form
    yang akan menimpa data lama.
    - kemudian akan mengecek apakah data baru tersebut sudah sesuai dengan tipe filed pada databasenya, jika benar maka akan disimpan kemudian akan
    dibawa ke halaman alternatif untuk melihat semua data alternatif yang ada termaruk data yang sudah di edit tersebut.
    jika salah maka akan tetap berada di halaman form dengan cara merefres atau me load ulang halaman tersbut.

"""
@login_required
def edit_alternatif(request,id):
    alternatif = Alternatif.objects.get(id=id)
    if request.method == 'POST':
        form = AlternatifForm(request.POST, instance=alternatif)
        if form.is_valid():
            form.save()
            return redirect('alternatif')
    else:
        form = AlternatifForm(instance=alternatif)

    context = {
        'form':form,
    }
    return render(request, 'dashboard_form.html', context)

"""
def hapus_alternatif:
    fungsi untuk menghapus data alternatif, degan cara.
    - mengambil data mana yang harus di hapus sama seperti dengan update dengan cara mengambil id nya
    - kemudian setelah itu akan langsung menghpus data tersebut dari tabel alternatif

* begitupun dengan fungsi lain seperti kriteria dan penilaian (bedanya cuma ke tabel tujuanya)
"""
@login_required
def hapus_alternatif(request,id):
    alternatif = Alternatif.objects.get(id=id)
    alternatif.delete()
    return redirect('alternatif')

# KRITERIA ---------------------------------------------------------------------
@login_required
def dashboard_kriteria(request):
    datas = Kriteria.objects.all()

    context ={
        'datas':datas,
    }
    return render(request, 'dashboard03.html', context)

@login_required
def tambah_kriteria(request):
    if request.method == 'POST':
        form = KriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kriteria')
    else:
        form = KriteriaForm()
    context = {
        'form':form,
    }

    return render(request, 'dashboard_form.html', context)

@login_required
def edit_kriteria(request,id):
    kriteria = Kriteria.objects.get(id=id)
    if request.method == 'POST':
        form = KriteriaForm(request.POST, instance=kriteria)
        if form.is_valid():
            form.save()
            return redirect('kriteria')
    else:
        form = KriteriaForm(instance=kriteria)

    context = {
        'form':form,
    }
    return render(request, 'dashboard_form.html', context)

@login_required
def hapus_kriteria(request,id):
    kriteria = Kriteria.objects.get(id=id)
    kriteria.delete()
    return redirect('kriteria')

# PENILAIAN ---------------------------------------------------------------------
@login_required
def dashboard_penilaian(request):
    data = Penilaian.objects.select_related('alternatif').all()
    data_normalisasi = Normalisasi.objects.select_related('alternatif').all()
    data_kriteria = Kriteria.objects.all()
    data_rengking = Rengking.objects.select_related('alternatif').all()

    # data= Penilaian.objects.all()
    # data_normalisasi= Normalisasi.objects.all()
    # data_kriteria = Kriteria.objects.all()
    # data_rengking = Rengking.objects.all()

    # Menghitung nilai maksimal dan minimal untuk setiap kriteria
    max_values = Penilaian.objects.aggregate(
        Max('kriteria1'), 
        Max('kriteria2'), 
        Max('kriteria3'), 
        Max('kriteria4')
    )
    min_values = Penilaian.objects.aggregate(
        Min('kriteria1'), 
        Min('kriteria2'), 
        Min('kriteria3'), 
        Min('kriteria4')
    )


    context ={
        'datas':data,
        'data_normalisasi':data_normalisasi,
        'max_values': max_values,
        'min_values': min_values,
        'data_kriteria': data_kriteria,
        'data_rengking': data_rengking,
    }
    return render(request, 'dashboard05.html', context)

@login_required
def tambah_penilaian(request):
    if request.method == 'POST':
        form = PenilaianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('penilaian')
    else:
        form = PenilaianForm()
    context = {
        'form':form,
    }

    return render(request, 'dashboard_form.html', context)

@login_required
def edit_penilaian(request,id):
    penilaian = Penilaian.objects.get(id=id)
    
    if request.method == 'POST':
        form = PenilaianForm(request.POST, instance=penilaian)
        if form.is_valid():
            form.save()
            return redirect('penilaian')
    else:
        form = PenilaianForm(instance=penilaian)

    context = {
        'form':form,
    }
    return render(request, 'dashboard_form.html', context)

@login_required
def hapus_penilaian(request,id):
    penilaian = Penilaian.objects.get(id=id)
    penilaian.delete()
    return redirect('penilaian')

@login_required
def dashboard_rengking(request):
    # Menggunakan select_related untuk mengurangi jumlah query jika ada hubungan ke model lain
    data_rengking = Rengking.objects.select_related('alternatif').all().order_by('-total_nilai')

    # Mengambil nilai maksimal dari total_nilai
    max_total = data_rengking.aggregate(Max('total_nilai'))['total_nilai__max']

    context = {
        'data_rengking': data_rengking,
        'max_total': max_total
    }
    return render(request, 'dashboard06.html', context)
    # max_total = Rengking.objects.aggregate(Max('total_nilai'))['total_nilai__max']
    # data_rengking = Rengking.objects.all().order_by('-total_nilai')

    # context ={
    #     'data_rengking': data_rengking,
    #     'max_total': max_total
    # }
    # return render(request, 'dashboard06.html', context)

"""
def hitung_normalisasi:
    fungsi yang melakukan normalisasi data penilaian. Pada bagian ini, kode melakukan perhitungan normalisasi 
    untuk setiap data penilaian dengan membagi setiap nilai kriteria dengan nilai maksimal dari masing-masing kriteria. 
    Hasil normalisasi kemudian disimpan ke dalam tabel Normalisasi dengan menggunakan metode [create] dari model normalisasi.

Untuk melakukan normalisasi, langkah-langkahnya adalah sebagai berikut:
1. Dapatkan semua data penilaian 
2. Hitung nilai maksimal dan minimal untuk setiap kriteria.
3. Untuk setiap data penilaian, bagi nilai kriteria dengan nilai maksimal dari kriteria tersebut.
4. Simpan hasil normalisasi ke dalam tabel Normalisasi dengan menyimpan nilai normalisasi untuk setiap kriteria.

"""
# PERHITUNGAN -------------------------------------------------------------------
def hitung_normalisasi(request):
    if request.method == 'POST':
        # Mendapatkan semua data penilaian
        penilaian_data = Penilaian.objects.all()

        # Mendapatkan nilai maksimal dan minimal untuk setiap kriteria
        max_values = Penilaian.objects.aggregate(
            Max('kriteria1'), 
            Max('kriteria2'), 
            Max('kriteria3'), 
            Max('kriteria4')
        )
        min_values = Penilaian.objects.aggregate(
            Min('kriteria1'), 
            Min('kriteria2'), 
            Min('kriteria3'), 
            Min('kriteria4')
        )

        # Menghitung normalisasi untuk setiap data penilaian dengan membagi nilai kriteria dengan nilai maksimal dari kriteria
       
        for data in penilaian_data: 
             # setiap iterasi dari loop tersebut akan mengambil satu data penilaian dari penilaian_data, berarti bahwa setiap iterasi akan mengambil satu baris data penilaian yang terdiri dari nilai kriteria (kriteria1, kriteria2, kriteria3, kriteria4) untuk proses normalisasi
            normalisasi_kriteria1 = data.kriteria1 / max_values['kriteria1__max']
            normalisasi_kriteria2 = data.kriteria2 / max_values['kriteria2__max']
            normalisasi_kriteria3 = data.kriteria3 / max_values['kriteria3__max']
            normalisasi_kriteria4 = data.kriteria4 / max_values['kriteria4__max']

            # Menyimpan hasil normalisasi ke dalam tabel Normalisasi
            Normalisasi.objects.create(
                alternatif=data.alternatif,
                kriteria1=normalisasi_kriteria1,
                kriteria2=normalisasi_kriteria2,
                kriteria3=normalisasi_kriteria3,
                kriteria4=normalisasi_kriteria4
            )

        # Redirect kembali ke halaman dashboard penilaian
        return redirect('penilaian')
    
"""
def hitung_rengking:
    fungsi yang menghitung rengking untuk setiap data normalisasi. Pada bagian ini, kode mengambil semua data normalisasi dan bobot untuk setiap kriteria. 
    Kemudian, untuk setiap data normalisasi, kode menghitung nilai rengking dengan mengalikan nilai kriteria dengan bobot kriteria yang sesuai. 
    Setelah itu, kode menjumlahkan nilai rengking dari masing-masing kriteria untuk mendapatkan total nilai rengking. 
    Hasil rengking kemudian disimpan ke dalam tabel Rengking menggunakan metode [create] dari model rengking.

Untuk melakukan perhitungan rengking langkah-langkahnya adalah sebagai berikut::
1. Mendapatkan semua data normalisasi.
2. Mendapatkan bobot untuk setiap kriteria.
3. Untuk setiap data normalisasi, mengalikan nilai kriteria dengan bobot kriteria yang sesuai.
4. Menjumlahkan nilai rengking dari masing-masing kriteria untuk mendapatkan total nilai rengking.
5. Menyimpan hasil rengking ke dalam tabel Rengking dengan mencatat nilai rengking untuk setiap kriteria dan total nilai rengking.
6. Setelah perhitungan selesai, mengarahkan kembali ke halaman dashboard untuk menampilkan hasil perhitungan rengking.

"""

def hitung_rengking(request):
    if request.method == 'POST':
        # Mendapatkan semua data normalisasi
        data_normalisasi = Normalisasi.objects.all()

        # Mendapatkan bobot untuk setiap kriteria
        data_kriteria = Kriteria.objects.all()

        # Menghitung rengking untuk setiap data normalisasi
        for data in data_normalisasi:
            

            # mengalikan nilai kriteria dengan bobot kriteria yang sesuai
            kriteria1 = data.kriteria1 * data_kriteria[0].bobot
            kriteria2 = data.kriteria2 * data_kriteria[1].bobot
            kriteria3 = data.kriteria3 * data_kriteria[2].bobot
            kriteria4 = data.kriteria4 * data_kriteria[3].bobot  
            
            # Menjumlahkan nilai rengking dari masing-masing kriteria untuk mendapatkan total niali akhir
            total_nilai = kriteria1 + kriteria2 + kriteria3 + kriteria4          

            # Menyimpan hasil rengking ke dalam tabel Rengking
            Rengking.objects.create(
                alternatif=data.alternatif,
                kriteria1=kriteria1,
                kriteria2=kriteria2,
                kriteria3=kriteria3,
                kriteria4=kriteria4,
                total_nilai = total_nilai
            )

        # Redirect kembali ke halaman dashboard
        return redirect('penilaian')


"""
def reset_normalisasi dan def reset_rengking:
    Kedua fungsi tersebut digunakan untuk menghapus semua data tabel Normalisasi (reset_normalisasi) dan Rengking (reset_rengking). 
    Setelah itu, pengguna akan diarahkan kembali ke halaman dashboard penilaian dengan menggunakan `redirect('penilaian')`.
"""
def reset_normalisasi(request):
    Normalisasi.objects.all().delete()
    return redirect('penilaian')

def reset_rengking(request):
    Rengking.objects.all().delete()
    return redirect('penilaian')


# atuh ---------------------------------------------------------------
"""
def signin_form:
    Fungsi [signin_form] digunakan untuk menangani proses autentikasi pengguna. Jika metode request adalah POST, maka fungsi akan mencoba mengautentikasi pengguna 
    berdasarkan username dan password yang diterima. Jika autentikasi berhasil, pengguna akan diarahkan ke halaman dashboard dengan pesan selamat datang. 
    Jika autentikasi gagal, pengguna akan diarahkan kembali ke halaman sign-in.

def signout_form:
    Fungsi [signout_form] digunakan untuk menangani proses logout pengguna. Ketika fungsi ini dipanggil, pengguna akan logout dari sistem dan diarahkan kembali ke halaman index.
"""
def signin_form(request):
    # jika user belum login, ketika menekan tombol login atau get started, maka akan langsung di arahkan ke halaman login
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        # jika user ada didalam database atau jika sukses login
        if user is not None:
            login(request, user)
            messages.success(request, f"Sign in Berhasil, Selamat Datang {user.username}!")
            return redirect('dashboard')
        # sebaliknya 
        else:
            messages.error(request, "Sign in Gagal, Silahkan Coba Kembali!")
            return redirect('signin')
        
    # jika user sudah login sebelumnya atau belum logout, ketika menekan tombol login atau get started 
    # maka akan langsung di arahkan ke halaman dashbaord tidak lagi ke halaman login
    elif request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'signin.html')

def signout_form(request):
    logout(request)
    return redirect('index')