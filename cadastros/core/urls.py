from django.urls import path
from cadastros.core import views

app_name = 'core'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastros/', views.cadastro_lista, name='cadastro_lista'),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
    path('<int:pk>/', views.cadastro_detalhe, name='cadastro_detalhe'),
    path('add/', views.CriarCadastro.as_view(), name='cadastro_add'),
    path('<int:pk>/edit/', views.AtualizarCadastro.as_view(), name='editar_cadastro'),
    path('excluir/<int:pk>/', views.DeletarCadastro.as_view(), name='deletar_cadastro'),
]