from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import LayerSerializer      
from .models import Layer                    


class LayerView(viewsets.ModelViewSet):       
    serializer_class = LayerSerializer          
    queryset = Layer.objects.all()     
