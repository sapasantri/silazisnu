from rest_framework import status, viewsets, views
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import (Propinsi,)
from .serializers import (PropinsiSerializer, )


class PropinsiViewSet(viewsets.ModelViewSet):
    queryset = Propinsi.objects.all()
    serializer_class = PropinsiSerializer
    filterset_fields = ('is_active', 'nama')
    pagination_class = None
    permission_classes = (IsAuthenticated,)
