from rest_framework.serializers import ModelSerializer

from fotos.models import Fotos


class FotosSerializer(ModelSerializer):
    class Meta:
        model = Fotos
        fields = ['nome_ponto','imagem']