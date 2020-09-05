from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
#from appLivraria.models import Livro
from .models import *


class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['autor', 'isbn', 'numeroPaginas', 'titulo', 'anoPublicacao', 'emailEditora']


def livro_list(request, template_name='livro_list.html'):
    livro = Livro.objects.all()
    livros = {'lista': livro}
    return render(request, template_name, livros)


def livro_new(request, template_name='livro_form.html'):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_livros')
    return render(request, template_name, {'form': form})


def livro_edit(request, pk, template_name='livro_form.html'):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)

        if form.is_valid():
            livro = form.save()
            return redirect("listar_livros")
    else:
        form = LivroForm(instance=livro)
    return render(request, template_name, {'form': form})


def livro_remove(request, pk):
    livro = Livro.objects.get(pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request, 'livro_delete.html', {'livro': livro})
