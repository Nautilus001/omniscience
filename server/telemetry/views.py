from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import Container
from .serializers import ContainerSerializer

# Create your views here.
def containers(request):
    return HttpResponse("Hello!")

class ContainerViewSet(viewsets.ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer