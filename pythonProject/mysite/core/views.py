from django.shortcuts import render, redirect
from .models import Usuario
# Create your views here.
def home(request):
    usuarios = Usuario.objects.all()
    return render(request, "index.html", {"usuarios": usuarios})

def salvar(request):
    vnome = request.POST.get("nome")
    Usuario.objects.create(nome=vnome)
    usuarios = Usuario.objects.all()
    return render(request, "index.html", {"usuarios": usuarios})

def editar(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, "update.html", {"usuario": usuario})

def update(request, id):
    vnome = request.POST.get("nome")
    usuario = Usuario.objects.get(id=id)
    usuario.nome = vnome
    usuario.save()
    return redirect(home)

def delete(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect(home)