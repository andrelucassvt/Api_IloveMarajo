from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from PontosTuristicos.API.Serializes import PontosTuristicosSerializer
from PontosTuristicos.models import PontosTuristicos


class PontosTuristicosViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PontosTuristicos.objects.all()
    serializer_class = PontosTuristicosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'nome','municipio','cidade']