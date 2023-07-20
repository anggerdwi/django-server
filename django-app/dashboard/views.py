from django.shortcuts import render, redirect
from dashboard.forms import FormBarang, FormKategori
from dashboard.models import Barang, Kategori
from django.contrib import messages
from django.db.models import Q
from dashboard.views import *

# def search(request):
#     search_post = request.GET.get('search')

#     if search_post:
#         posts = post.objects.filter(Q(title__icontains=search_post) & Q(content__icontains=search_post))
#     else:
#         posts = post.objects.all().order_by("-data_created")
#         return render(request,'/vbrg')




def delete_brg(request,id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request,"Data berhasil dihapus!")
    return redirect('/vbrg')

def ubah_brg(request,id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diubah!')
            return redirect('/vbrg')
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form':form,
            'barangs':barangs
        }
    return render(request,'ubah_brg.html',konteks)

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


# BAGIAN KATEGORI
def tambah_Kategori(request):
    form=FormKategori(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('/vkategori')
        pass
    
    konteks={
        'form' : form,
    }
    return render(request,'tambah_kategori.html',konteks)

def kategori_view(request):
    category=Kategori.objects.all().values()

    konteks={
        'category':category,
    }

    return render(request,'tampil_kategori.html',konteks)

    