from rest_framework import serializers, fields
from .models import (Organization, Jabatan)


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'pc', 'mwc', 'ranting', 'level', 'nama')


class JabatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jabatan
        fields = ('id', 'nama')
