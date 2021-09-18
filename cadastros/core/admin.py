from django.contrib import admin
from .models import Familias

# imports do pdf
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string
from django_object_actions import DjangoObjectActions

@admin.register(Familias)
class FamiliasAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ['id', 'nome', 'slug', 'rua', 'cidade', 'renda', 'comentario', 'criado_em', 'atualizado_em']
    list_filter = ['criado_em']
    list_editable = ['nome','slug','rua', 'cidade', 'renda', 'comentario']
    prepopulated_fields = {'slug': ('nome',)}
    # testando gerador de pdf
    def generate_pdf(self, request, obj):
        html_string = render_to_string('reports/pdf_template.html', {'obj': obj})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(obj));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
            return response

        return response

    generate_pdf.label = 'Gerar PDF'
    generate_pdf.short_description = 'Clique para gerar o PDF dessa ordem de serviço'

    change_actions = ('generate_pdf',)