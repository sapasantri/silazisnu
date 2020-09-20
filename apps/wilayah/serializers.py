from rest_framework import serializers, fields
from .models import (Propinsi, Kota, Kecamatan, Desa)


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


class KecamatanSerializer(serializers.ModelSerializer):
    propinsi_id = serializers.IntegerField(write_only=True)
    kota = KotaSerializer(many=False, read_only=True)
    kota_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Kecamatan
        fields = ('id', 'propinsi_id', 'kota_id', 'kode', 'nama', 'kota')


class DesaSerializer(serializers.ModelSerializer):
    propinsi_id = serializers.IntegerField(write_only=True)
    kota_id = serializers.IntegerField(write_only=True)
    kecamatan_id = serializers.IntegerField(write_only=True)
    kecamatan = KecamatanSerializer(many=False, read_only=True)

    class Meta:
        model = Desa
        fields = ('id', 'propinsi_id', 'kota_id', 'kecamatan_id', 'kode',
                  'nama', 'kecamatan')
