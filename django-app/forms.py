from django.forms import ModelForm
from dashboard.models import Barang

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'