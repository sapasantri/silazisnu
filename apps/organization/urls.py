from rest_framework import routers
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import api

router = routers.DefaultRouter()
router.register(r'level', api.OrganizationViewSet)
router.register(r'jabatan', api.JabatanViewSet)

app_name = 'organization'
urlpatterns = [
    path('organisasi/', include(router.urls)),
    path('email/', api.SendEmailViewSet.as_view(), name='send_email'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
