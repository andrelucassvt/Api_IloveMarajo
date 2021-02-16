from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from Municipios.API.Serializes import MunicipiosSerializer
from Municipios.models import Municipios


class MunicipiosViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Municipios.objects.all()
    serializer_class = MunicipiosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'nome']
