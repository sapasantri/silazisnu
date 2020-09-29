from rest_framework import routers
from django.urls import include, path
from django.conf.urls import url
from . import api

router = routers.DefaultRouter()
router.register(r'penerimaan', api.PenerimaanViewSet)
router.register(r'penerimaan-per-bulan', api.PenerimaanByMonthViewSet)


app_name = 'transaksi'
urlpatterns = [
    path('transaksi/', include(router.urls)),
]
