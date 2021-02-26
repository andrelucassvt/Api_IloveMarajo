from django.db import models

from Municipios.models import Municipios
from fotos.models import Fotos


class PontosTuristicos(models.Model):

    id = models.IntegerField(primary_key=True)
    municipio = models.ForeignKey(
        Municipios, on_delete=models.CASCADE,null=False,blank=False
    )
    fotos = models.ManyToManyField(Fotos)
    nome = models.TextField(max_length=150)
    perfil = models.ImageField(upload_to='Api_IloveMarajo',null=True,blank=True)
    descricao = models.TextField(max_length=500)
    cidade = models.TextField(max_length=150)
    latitude = models.TextField(max_length=100)
    longitude = models.TextField(max_length=100)
    estrelas = models.TextField(max_length=12)

    def __str__(self):
        return self.nome
