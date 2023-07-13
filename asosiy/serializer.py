from .models import *
from rest_framework import serializers
from userapp.serializer import OmborSerializer

class MahsulotSerializer(serializers.ModelSerializer):
    ombor = OmborSerializer(many=True)

    class Meta:
        model = Mahsulot
        fields = '__all__'


class MijozSerializer(serializers.ModelSerializer):
    ombor = OmborSerializer(many=True)

    class Meta:
        model = Mijoz
        fields = '__all__'

