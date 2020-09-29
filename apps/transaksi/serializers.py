from rest_framework import serializers, fields
from django.db.models.functions import TruncMonth, TruncYear
from .models import (Penerimaan)
from apps.organization.models import Organization


class FilteredPenerimaanSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        if self.context['request'].GET.get('bulan') is not None:
            bulan = self.context['request'].GET.get('bulan')
            data = data.filter(date_transaction__month=bulan)

        if self.context['request'].GET.get('tahun') is not None:
            tahun = self.context['request'].GET.get('tahun')
            data = data.filter(date_transaction__year=tahun)

        return super(FilteredPenerimaanSerializer, self).to_representation(data)


class PenerimaanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penerimaan
        list_serializer_class = FilteredPenerimaanSerializer
        fields = '__all__'


class PenerimaanOrganisasiSerializer(serializers.ModelSerializer):

    penerimaan = PenerimaanSerializer(
        source='organisasi',
        many=True
    )

    class Meta:
        model = Organization
        fields = '__all__'


class PenerimaanByMonthSerializer(serializers.ModelSerializer):
    # detail = serializers.SerializerMethodField()
    month = serializers.SerializerMethodField()

    class Meta:
        model = Penerimaan
        fields = ('month', )

    def get_month(self, instance):
        print (type(instance))
        return instance.count
    #     return instance.date_transaction.strftime('%B')

    # def get_detail(self, instance):
    # #     date = instance.date_transaction
    # #     detail = Penerimaan.objects.annotate(
    # #         month=TruncMonth('date_transaction')
    # #     ).filter(month=date).values('date_transaction').distinct()
    # #     print(detail.query)
    #     # events = Event.objects.filter(date__month=month, date__year=year)
    #     # event_serializer = EventSerializer(events, many=True)
    #     return instance
