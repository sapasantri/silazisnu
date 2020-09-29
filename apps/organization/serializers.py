from rest_framework import fields, serializers

from .models import Jabatan, Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'pc', 'mwc', 'ranting', 'level', 'nama')


class JabatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jabatan
        fields = ('id', 'nama')
