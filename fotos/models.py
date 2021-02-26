from django.db import models


class Fotos(models.Model):

    id = models.IntegerField(primary_key=True)
    nome_ponto = models.TextField(max_length=150,null=True,blank=True)
    imagem = models.ImageField(upload_to='Api_IloveMarajo',null=True,blank=True)

    def __str__(self):
        return self.nome_ponto