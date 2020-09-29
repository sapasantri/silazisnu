from rest_framework import serializers, fields
from apps.organization.serializers import JabatanSerializer
from rest_framework_simplejwt.tokens import  RefreshToken
from .models import (User)


from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(required=True)

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if not data['username']:
            raise serializers.ValidationError("Username Kosong")
        return data


class PengurusSerializer(serializers.ModelSerializer):
    jabatan = JabatanSerializer(many=False, read_only=True)
    tokens = serializers.SerializerMethodField()


    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'full_name', 'password', 'jabatan',
        'tokens')
        extra_kwargs = {'password': {'write_only': True}}

    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)
        refresh = str(tokens)
        access = str(tokens.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
