from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Alternatif, Kriteria, Crips
from .forms import AlternatifForm, KriteriaForm, CripsForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard01.html')

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
        
    # tidak bisa mengkases halaman login kemabli
    elif request.user.is_authenticated:
        return redirect('dashboard')
        # return redirect('admin:index')

    return render(request, 'signin.html')

def signout_form(request):
    logout(request)
    return redirect('index')