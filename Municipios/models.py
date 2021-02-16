from django.db import models

class Municipios(models.Model):

    id = models.IntegerField(primary_key=True)
    nome = models.TextField(max_length=150)

    def __str__(self):
        return self.nome