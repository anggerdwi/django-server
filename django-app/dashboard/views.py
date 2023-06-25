from django.shortcuts import render

def produk(request):
    title="produk"
    konteks = {
        'tagTitle':title,
    }
    return render(request,'produk.html',konteks)
# Create your views here.
