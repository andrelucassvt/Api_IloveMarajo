from rest_framework.serializers import ModelSerializer

from PontosTuristicos.models import PontosTuristicos
from fotos.API.Serializers import FotosSerializer


class PontosTuristicosSerializer(ModelSerializer):
    fotos = FotosSerializer(many=True)

    class Meta:
        model = PontosTuristicos
        fields = ['nome','municipio','perfil','fotos','descricao','cidade','latitude','longitude','estrelas']