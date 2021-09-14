from django.shortcuts import render, get_object_or_404
from .models import Familias

# Create your views here.

def home(request):
    return render(request,'cadastro.html')


def familias_lista(request, category_slug=None):
    familias = Familias.objects.all()
    return render(request, 'lista.html', {'familias': familias})

def familia_unica(request, id, slug):
    familia = get_object_or_404(Familias, id=id, slug=slug)
    return render(request,'detalhe.html', {'familia': familia})


