from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import *

class StatistikaModelViewSet(ModelViewSet):
    queryset = Statistika.objects.all()
    serializer_class = StatistikaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Statistika.objects.filter(user=self.request.user)
        return queryset
# Create your views here.
