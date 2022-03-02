import imp
from django import forms
from pyrsistent import field
from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = ['nit','name','address','telephone']