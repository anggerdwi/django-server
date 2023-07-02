"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import produk, tambah_barang, Barang_View, ubah_brg, delete_brg

def main(request):
    return HttpResponse("selamat datang")

def main_one(request):
    title="beranda"
    konteks = {
        'tagTitle':title,
    }
    return render(request,'index.html',konteks)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_one),
    path('beranda/',main_one),
    path('products/',produk),
    path('addbrg/',tambah_barang),
    path('vbrg/',Barang_View),
    path('ubah/<int:id_barang>', ubah_brg, name = 'ubah_brg'),
    path('delete/<int:id_barang>', delete_brg, name = 'delete_brg'),
    # path('search/<int:id_barang>', search_brg, name = 'search'),
]
