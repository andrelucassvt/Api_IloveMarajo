from rest_framework.serializers import ModelSerializer

from Municipios.models import Municipios


class MunicipiosSerializer(ModelSerializer):
    class Meta:
        model = Municipios
        fields = ['nome']