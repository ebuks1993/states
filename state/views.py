from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import States
from .serializers import StateSerializer

# Create your views here.

class StateViewset(ModelViewSet):
    queryset=States.objects.all()
    serializer_class=StateSerializer
