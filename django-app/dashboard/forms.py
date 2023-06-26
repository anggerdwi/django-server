from django.forms import ModelForm
from dashboard.models import Barang
from django import forms

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'

        widgets = {
            'kodebrg' : forms.TextInput({'class' : 'mt-2 p-2 border border-gray-300 focus:outline-none focus:ring-0 focus:border-gray-300 rounded text-sm text-gray-900'}),
            'nama' : forms.TextInput({'class' : 'mt-2 p-2 border border-gray-300 focus:outline-none focus:ring-0 focus:border-gray-300 rounded text-sm text-gray-900'}),
            'stok' : forms.NumberInput({'class' : 'mt-2 p-2 border border-gray-300 focus:outline-none focus:ring-0 focus:border-gray-300 rounded text-sm text-gray-900'}),
            'harga' : forms.NumberInput({'class' : 'mt-2 p-2 border border-gray-300 focus:outline-none focus:ring-0 focus:border-gray-300 rounded text-sm text-gray-900'}),
            'link_gbr' : forms.TextInput({'class' : 'mt-2 p-2 border border-gray-300 focus:outline-none focus:ring-0 focus:border-gray-300 rounded text-sm text-gray-900'}),
            'jenis_id' : forms.Select({'class' : 'mt-2 p-2 border border-gray-300 focus:outline-none focus:ring-0 focus:border-gray-300 rounded text-sm text-gray-900'}),
        }