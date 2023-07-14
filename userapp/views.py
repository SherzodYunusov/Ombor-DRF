from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import *

class OmborModelSetView(ModelViewSet):
    queryset = Ombor.objects.all()
    serializer_class = OmborSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Ombor.objects.filter(ombor__user=self.request.user)
        return queryset
# Create your views here.
