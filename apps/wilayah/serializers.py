from rest_framework import serializers, fields
from .models import (Propinsi, Kota)


class PropinsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propinsi
        fields = ('id', 'kode', 'nama')

class KotaSerializer(serializers.ModelSerializer):
    propinsi = PropinsiSerializer(many=False, read_only=True)
    propinsi_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Kota
        fields = ('id', 'propinsi_id', 'kode', 'nama', 'propinsi')
