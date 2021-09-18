from cadastros.core.forms import CadastroForm
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Familias
from .forms import CadastroForm
from django.views.generic import TemplateView, ListView, UpdateView, DetailView

def inicio(request):
    return render(request, 'index.html')


def cadastro_lista(request):
    template_name = 'lista.html'
    objects = Familias.objects.all()
    search = request.GET.get('search')
    if search:
        objects=objects.filter(nome__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context)


def cadastro_detalhe(request, pk):
    template_name = 'cadastro_detalhe.html'
    obj = Familias.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def cadastro_add(request):
    template_name = 'cadastro_form.html'
    return render(request, template_name)


class CriarCadastro(CreateView):
    model = Familias
    template_name = 'cadastro_form.html'
    form_class = CadastroForm

class AtualizarCadastro(UpdateView):
    model = Familias
    template_name = 'cadastro_form.html'
    form_class = CadastroForm