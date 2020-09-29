from rest_framework import status, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core import serializers
from silazisnu.permissions import IsServedAs
from rest_framework_simplejwt.views import ( TokenObtainPairView,)


from .models import (User)
from .serializers import (PengurusSerializer, LoginSerializer)


class LoginViewSet(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        # serializer = LoginSerializer(data=request.data,
        #                                    context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        # print(user)
        tokens = RefreshToken.for_user(user)
        token = {
            "access": str(tokens.access_token),
            "refresh": str(tokens)
        }

        detail_user = {
            'id': user.pk,
            'username': user.username,
            'email': user.email,
            'phone': user.phone,
            'full_name': user.full_name,
            'jabatan': user.jabatan.nama,
        }

        return Response({
            'user': detail_user,
            'token': token
        })

        # return Response()


class PengurusViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PengurusSerializer
    filterset_fields = ('is_active', 'username')
    permission_classes = (IsAuthenticated,)
