import operator
from django.db.models import Q
from django.db.models.functions import TruncMonth, TruncYear
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets, views

from .models import Penerimaan
from apps.organization.models import Organization
from .serializers import (
    PenerimaanOrganisasiSerializer, PenerimaanByMonthSerializer)
from django.db.models import Count

class PenerimaanViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = PenerimaanOrganisasiSerializer
    filterset_fields = ('is_active',)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        qs = super(PenerimaanViewSet,
                   self).get_queryset(*args, **kwargs)

        if self.request.GET.get('tingkat') == "1":
            return qs
        elif self.request.GET.get('tingkat') == "2":
            qs = qs.filter(
                pc=self.request.user.menjabat.pc,
                mwc=self.request.user.menjabat.mwc,
                level=self.request.user.menjabat.level
            )
            return qs
        elif self.request.GET.get('tingkat') == "3":
            qs = qs.filter(
                pc=self.request.user.menjabat.pc,
                mwc=self.request.user.menjabat.mwc,
                ranting=self.request.user.menjabat.ranting,
                level=self.request.user.menjabat.level
            )
            return qs
        elif self.request.GET.get('tingkat') == "4":
            qs = qs.filter(
                pc=self.request.user.menjabat.pc,
                mwc=self.request.user.menjabat.mwc,
                ranting=self.request.user.menjabat.ranting,
                jpzis=self.request.user.menjabat.jpzis,
                level=self.request.user.menjabat.level
            )
            return qs
        #         penerimaan__date_transaction__month=self.request.GET.get('bulan'),
        #         penerimaan__date_transaction__year=self.request.GET.get('tahun'))
        return qs


class PenerimaanByMonthViewSet(viewsets.ModelViewSet):
    queryset = Penerimaan.objects.all()
    serializer_class = PenerimaanByMonthSerializer
    filterset_fields = ('is_active',)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        qs = super(PenerimaanByMonthViewSet,
                   self).get_queryset(*args, **kwargs)
        qs = qs.annotate(month=TruncMonth('date_transaction')).values(
            'date_transaction').annotate(count=Count('id')).order_by()
        # qs = qs.annotate(
        #     month=TruncMonth('date_transaction')
        #     )
        print(qs.query)
        return qs
