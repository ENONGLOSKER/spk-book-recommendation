from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min

from .models import Alternatif, Kriteria, Crips, Penilaian, Normalisasi, Rengking
from .forms import AlternatifForm, KriteriaForm, CripsForm, PenilaianForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    alternatif = Alternatif.objects.all().count()
    kriteria = Kriteria.objects.all().count()
    penilaian = Penilaian.objects.all().count() / Alternatif.objects.all().count()


    context = {
        'alternatif':alternatif,
        'kriteria':kriteria,
        'penilaian':penilaian,
    }
    return render(request, 'dashboard01.html', context)

# ALTERNATIF ---------------------------------------------------------------------
@login_required
def dashboard_alternatif(request):
    datas = Alternatif.objects.all()

    context ={
        'datas':datas,
    }
    return render(request, 'dashboard02.html', context)

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

# CRIPS ---------------------------------------------------------------------
@login_required
def dashboard_crips(request, id):
    kriteria = get_object_or_404(Kriteria, id=id)
    data_crips = kriteria.crips.all()

    context ={
        'kriteria':kriteria,
        'datas':data_crips,
    }
    return render(request, 'dashboard04.html', context)
@login_required
def tambah_crips(request):
    if request.method == 'POST':
        form = CripsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kriteria')
    else:
        form = CripsForm()
    context = {
        'form':form,
    }

    return render(request, 'dashboard_form.html', context)

@login_required
def edit_crips(request,id):
    crips = Crips.objects.get(id=id)
    
    if request.method == 'POST':
        form = CripsForm(request.POST, instance=crips)
        if form.is_valid():
            form.save()
            return redirect('kriteria')
    else:
        form = CripsForm(instance=crips)

    context = {
        'form':form,
    }
    return render(request, 'dashboard_form.html', context)

@login_required
def hapus_crips(request,id):
    crips = Crips.objects.get(id=id)
    crips.delete()
    return redirect('kriteria')

# PENILAIAN ---------------------------------------------------------------------
@login_required
def dashboard_penilaian(request):
    data= Penilaian.objects.all()
    data_normalisasi= Normalisasi.objects.all()
    data_kriteria = Kriteria.objects.all()
    data_rengking = Rengking.objects.all()

    # Menghitung nilai maksimal dan minimal untuk setiap kriteria
    max_values = Penilaian.objects.aggregate(
        Max('kriteria1__nilai'), 
        Max('kriteria2__nilai'), 
        Max('kriteria3__nilai'), 
        Max('kriteria4__nilai')
    )
    min_values = Penilaian.objects.aggregate(
        Min('kriteria1__nilai'), 
        Min('kriteria2__nilai'), 
        Min('kriteria3__nilai'), 
        Min('kriteria4__nilai')
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
    data_rengking = Rengking.objects.all().order_by('id')

    context ={
        'data_rengking': data_rengking,
    }
    return render(request, 'dashboard06.html', context)


# PERHITUNGAN 

def hitung_normalisasi(request):
    if request.method == 'POST':
        # Mendapatkan semua data penilaian
        penilaian_data = Penilaian.objects.all()

        # Mendapatkan nilai maksimal dan minimal untuk setiap kriteria
        max_values = Penilaian.objects.aggregate(
            Max('kriteria1__nilai'), 
            Max('kriteria2__nilai'), 
            Max('kriteria3__nilai'), 
            Max('kriteria4__nilai')
        )
        min_values = Penilaian.objects.aggregate(
            Min('kriteria1__nilai'), 
            Min('kriteria2__nilai'), 
            Min('kriteria3__nilai'), 
            Min('kriteria4__nilai')
        )

        # Menghitung normalisasi untuk setiap data penilaian
        for data in penilaian_data:
            normalisasi_kriteria1 = data.kriteria1.nilai / max_values['kriteria1__nilai__max']
            normalisasi_kriteria2 = data.kriteria2.nilai / max_values['kriteria2__nilai__max']
            normalisasi_kriteria3 = data.kriteria3.nilai / max_values['kriteria3__nilai__max']
            normalisasi_kriteria4 = data.kriteria4.nilai / max_values['kriteria4__nilai__max']

            # Menyimpan hasil normalisasi ke dalam tabel Normalisasi
            Normalisasi.objects.create(
                alternatif=data.alternatif,
                kriteria1=normalisasi_kriteria1,
                kriteria2=normalisasi_kriteria2,
                kriteria3=normalisasi_kriteria3,
                kriteria4=normalisasi_kriteria4
            )

        # Redirect kembali ke halaman dashboard
        return redirect('penilaian')

def hitung_rengking(request):
    if request.method == 'POST':
        # Mendapatkan semua data normalisasi
        data_normalisasi = Normalisasi.objects.all()

        # Mendapatkan bobot untuk setiap kriteria
        data_kriteria = Kriteria.objects.all()

        # Menghitung rengking untuk setiap data normalisasi
        for data in data_normalisasi:
            

            # Menghitung nilai rengking
            kriteria1 = data.kriteria1 * data_kriteria[0].bobot
            kriteria2 = data.kriteria2 * data_kriteria[1].bobot
            kriteria3 = data.kriteria3 * data_kriteria[2].bobot
            kriteria4 = data.kriteria4 * data_kriteria[3].bobot  
            
            # Menjumlahkan nilai rengking dari masing-masing kriteria
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



def reset_normalisasi(request):
    Normalisasi.objects.all().delete()
    return redirect('penilaian')

def reset_rengking(request):
    Rengking.objects.all().delete()
    return redirect('penilaian')

# atuh ---------------------------------------------------------------
def signin_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Sign in Berhasil, Selamat Datang {user.username}!")
            return redirect('dashboard')
            # return redirect('admin:index')
        else:
            messages.error(request, "Sign in Gagal, Silahkan Coba Kembali!")
            return redirect('signin')
        
    elif request.user.is_authenticated:
        return redirect('dashboard')
        # return redirect('admin:index')

    return render(request, 'signin.html')

def signout_form(request):
    logout(request)
    return redirect('index')