from django.urls import path
from . import views

app_name = 'cadastros.core'

urlpatterns = [
    path('', views.familias_lista, name='familia_lista'),
    path('<slug:category_slug>/', views.familias_lista, name='familias_por_data')

]