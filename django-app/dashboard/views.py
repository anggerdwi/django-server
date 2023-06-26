from django.shortcuts import render, redirect
from dashboard.forms import FormBarang
from dashboard.models import Barang

def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }

    return render(request,'tampil_brg.html',konteks)

def tambah_barang(request):
    form=FormBarang(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('/vbrg')
        pass
    
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
