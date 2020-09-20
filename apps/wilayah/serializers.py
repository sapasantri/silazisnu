from rest_framework import serializers, fields
from .models import (Propinsi, )


class PropinsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propinsi
        fields = ('id', 'kode', 'nama')
