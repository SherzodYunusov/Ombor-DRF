from rest_framework import serializers
from .models import *

from asosiy.serializer import MahsulotSerializer
from asosiy.serializer import MijozSerializer
from userapp.serializer import OmborSerializer

class StatistikaSerializer(serializers.ModelSerializer):
    mahsulot = MahsulotSerializer(many=True)
    mijoz = MijozSerializer(many=True)
    ombor = OmborSerializer(many=True)

    class Meta:
        model = Statistika
        fields = '__all__'

    def validate_mijoz(self, qiymat):
        if qiymat.qarz >= 500:
            raise serializers.ValidationError('Mahsulot olib ketishingiz mumkin emas')
        return qiymat
