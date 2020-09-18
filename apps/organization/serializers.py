from rest_framework import serializers, fields
from .models import (Organization, )


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'pc', 'mwc', 'ranting', 'level', 'nama')
