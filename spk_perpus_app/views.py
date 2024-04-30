from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard_alternatif(request):
    return render(request, 'dashboard.html')

def signin_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Sign in Berhasil, Selamat Datang {user.username}!")
            return redirect('admin:index')
        else:
            messages.error(request, "Sign in Gagal, Silahkan Coba Kembali!")
            return redirect('signin')
        
    # jika user sudah login maka tidak bisa mengkases halaman login lagi
    elif request.user.is_authenticated:
        return redirect('admin:index')

    return render(request, 'signin.html')