from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 
from spk_perpus_app import views

urlpatterns = [
    # auth
    path('signin/',views.signin_form, name='signin'),
    path('signout/',views.signout_form, name='signout'),
    # home
    path('',views.index, name='index'),
    # dashboard
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
    # penilaian
    path('dashboard/penilaian/',views.dashboard_penilaian, name='penilaian'),
    path('dashboard/penilaian/add/',views.tambah_penilaian, name='add_penilaian'),
    path('dashboard/penilaian/edit/<int:id>',views.edit_penilaian, name='edit_penilaian'),
    path('dashboard/penilaian/delete/<int:id>',views.hapus_penilaian, name='hapus_penilaian'),
    # perengkingan
    path('dashboard/rengking/',views.dashboard_rengking, name='rengking'),
    path('dashboard/penilaian/rengking/',views.hitung_rengking, name='hitung_rengking'),
    path('dashboard/penilaian/rengking/reset',views.reset_rengking, name='reset_rengking'),
    # perhitungan
    path('dashboard/penilaian/normalisasi/',views.hitung_normalisasi, name='hitung_normalisasi'),
    path('dashboard/penilaian/normalisasi/reset',views.reset_normalisasi, name='reset_normalisasi'),

    path('admin/', admin.site.urls), #dashboard bawaan django
    path("__debug__/", include("debug_toolbar.urls")),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
