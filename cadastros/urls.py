"""cadastros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LogoutView
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from cadastros.core.views import cadastro_lista, cadastro_detalhe

urlpatterns = [
    path('', include('cadastros.core.urls')),
    path('contato/', include('cadastros.core.urls')),
    path('sobre/', include('cadastros.core.urls')),
    path('cadastro_lista/', include('cadastros.core.urls')),
    path('cadastro_detalhe/', include('cadastros.core.urls')),
    path('editar_cadastro/', include('cadastros.core.urls')),
    path('deletar_cadastro/', include('cadastros.core.urls')),
    path('cadastros/', include('cadastros.core.urls')),
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),
]
