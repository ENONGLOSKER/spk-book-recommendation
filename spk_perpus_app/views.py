from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard01.html')

def dashboard_alternatif(request):
    return render(request, 'dashboard02.html')

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
        
    # jika user sudah login maka tidak bisa mengkases halaman login lagi
    elif request.user.is_authenticated:
        return redirect('dashboard')
        # return redirect('admin:index')

    return render(request, 'signin.html')

def signout_form(request):
    logout(request)
    return redirect('index')