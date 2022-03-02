from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Empresa
from .forms import EmpresaForm

def home(request):
    empresas = Empresa.objects.all()
    context={'empresas':empresas}
    return render(request, 'home.html', context)

def add(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = EmpresaForm()

    context={'form':form}
    return render(request, 'add.html', context)

def delete(request, empresa_id):
    empresa = Empresa.objects.get(nit=empresa_id)
    empresa.delete()
    return redirect("home")

def edit(request, empresa_id):
    empresa = Empresa.objects.get(nit=empresa_id)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = EmpresaForm(instance=empresa)

    context = {"form": form}
    return render(request, 'edit.html', context)