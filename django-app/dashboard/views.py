from django.shortcuts import render
from dashboard.forms import FormBarang
from dashboard.models import Barang

def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }

    return render(request,'tampil_brg.html',konteks)

def tambah_barang(request):
    form=FormBarang()
    konteks={
        'form' : form,
    }
    return render(request,'tambah_barang.html',konteks)

def produk(request):
    title="produk"
    konteks = {
        'tagTitle':title,
    }
    return render(request,'produk.html',konteks)
# Create your views here.
