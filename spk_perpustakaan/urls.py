"""
URL configuration for spk_perpustakaan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from spk_perpus_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('dashboard/',views.dashboard, name='dashboard'),
    # alternatif
    path('dashboard/alternatif/',views.dashboard_alternatif, name='alternatif'),
    path('dashboard/alternatif/add/',views.tambah_alternatif, name='add_alternatif'),
    path('dashboard/alternatif/edit/<int:id>',views.edit_alternatif, name='edit_alternatif'),
    path('dashboard/alternatif/delete/<int:id>',views.hapus_alternatif, name='hapus_alternatif'),
    # kriteria
    path('dashboard/kriteria/',views.dashboard_kriteria, name='kriteria'),
    path('dashboard/kriteria/add/',views.tambah_kriteria, name='add_kriteria'),
    path('dashboard/kriteria/edit/<int:id>',views.edit_kriteria, name='edit_kriteria'),
    path('dashboard/kriteria/delete/<int:id>',views.hapus_kriteria, name='hapus_kriteria'),
    # crips
    path('dashboard/kriteria/crips/<int:id>',views.dashboard_crips, name='crips'),
    path('dashboard/kriteria/crips/add/',views.tambah_crips, name='add_crips'),
    path('dashboard/kriteria/crips/edit/<int:id>',views.edit_crips, name='edit_crips'),
    path('dashboard/kriteria/crips/delete/<int:id>',views.hapus_crips, name='hapus_crips'),

    path('signin/',views.signin_form, name='signin'),
    path('signout/',views.signout_form, name='signout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
