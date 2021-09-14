from django.db import models
from django.urls.base import reverse

# Create your models here.

class Familias(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    rua = models.CharField(max_length=200, db_index=True)
    cidade = models.CharField(max_length=200, db_index=True)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    comentario = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('criado_em',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("core:familias_lista", args=[self.slug])
    