from django.contrib import admin

# Register your models here.
from .models import Barang, Jenis

admin.site.register(Barang)

class kolomBarang(admin.ModelAdmin):
    list_display = ['kodebrg','nama','stok','harga','link_gbr','jenis_id']
    search_fields=['kodebrg','nama']
    list_per_page=3

    # admin.site.register(Barang,kolomBarang)
    admin.site.register(Jenis)