from rest_framework import routers
from django.urls import include, path
from django.conf.urls import url
from . import api

router = routers.DefaultRouter()
router.register(r'pengurus', api.PengurusViewSet)
# router.register(r'login', api.LoginViewSet)

app_name = 'pengurus'
urlpatterns = [
    path('pengurus/login/', api.LoginViewSet.as_view(), name='login_token'),
    path('organisasi/', include(router.urls)),
]
