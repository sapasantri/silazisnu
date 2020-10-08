from rest_framework import routers
from django.urls import include, path
from django.conf.urls import url
from . import api
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'pengurus', api.PengurusViewSet)
# router.register(r'login', api.LoginViewSet)

app_name = 'pengurus'
urlpatterns = [
    path('pengurus/login/', api.LoginViewSet.as_view(), name='login_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('organisasi/', include(router.urls)),
]
