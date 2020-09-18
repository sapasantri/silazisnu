from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import (Organization,)
from .serializers import (OrganizationSerializer, )


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filterset_fields = ('is_active', 'nama')
    pagination_class = None
    permission_classes = (IsAuthenticated,)
