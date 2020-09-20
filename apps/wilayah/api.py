from rest_framework import status, viewsets, views
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from silazisnu.pagination import CustomPagination

from .models import (Propinsi, Kota, Kecamatan)
from .serializers import (PropinsiSerializer, KotaSerializer,
                          KecamatanSerializer)


class PropinsiViewSet(viewsets.ModelViewSet):
    queryset = Propinsi.objects.all()
    serializer_class = PropinsiSerializer
    filterset_fields = ('is_active', 'kode', 'nama')
    pagination_class = None
    permission_classes = (IsAuthenticated,)


class KotaViewSet(viewsets.ModelViewSet):
    queryset = Kota.objects.all()
    serializer_class = KotaSerializer
    filterset_fields = ('is_active', 'kode', 'nama')
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)


class KecamatanViewSet(viewsets.ModelViewSet):
    queryset = Kecamatan.objects.all()
    serializer_class = KecamatanSerializer
    filterset_fields = ('is_active', 'kode', 'nama')
    permission_classes = (IsAuthenticated,)
