from rest_framework import routers
from django.urls import include, path

from . import api

router = routers.DefaultRouter()
router.register(r'propinsi', api.PropinsiViewSet)
router.register(r'kota', api.KotaViewSet)
router.register(r'kecamatan', api.KecamatanViewSet)

app_name = 'wilayah'
urlpatterns = [
    path('wilayah/', include(router.urls)),
]
