from rest_framework.serializers import ModelSerializer

from PontosTuristicos.models import PontosTuristicos


class PontosTuristicosSerializer(ModelSerializer):
    class Meta:
        model = PontosTuristicos
        fields = ['nome','municipio','perfil','descricao','cidade','latitude','longitude','estrelas']