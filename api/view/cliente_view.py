from rest_framework import viewsets

from api.models import Cliente
from api.serializer.cliente_serializer import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
