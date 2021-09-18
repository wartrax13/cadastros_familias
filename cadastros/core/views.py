from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from cadastros.core.forms import CadastroForm
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Familias
from .forms import CadastroForm
from django.views.generic import TemplateView, ListView, UpdateView, DetailView


def inicio(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')

@login_required
def cadastro_lista(request):
    template_name = 'lista.html'
    objects = Familias.objects.all()
    search = request.GET.get('search')
    if search:
        objects=objects.filter(nome__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context)


@login_required
def cadastro_detalhe(request, pk):
    template_name = 'cadastro_detalhe.html'
    obj = Familias.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)

@login_required
def cadastro_add(request):
    template_name = 'cadastro_form.html'
    return render(request, template_name)


class CriarCadastro(LoginRequiredMixin, CreateView):
    model = Familias
    template_name = 'cadastro_form.html'
    form_class = CadastroForm
    success_url = reverse_lazy('inicio')


class AtualizarCadastro(UpdateView):
    model = Familias
    template_name = 'cadastro_form.html'
    form_class = CadastroForm
    #success_url = reverse_lazy('core:inicio')

class DeletarCadastro(DeleteView):
    model = Familias
    template_name = 'deletar_form.html'
    form_class = CadastroForm
    success_url = reverse_lazy('core:inicio')