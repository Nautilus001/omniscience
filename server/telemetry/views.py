from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from server.telemetry.models import Container
from server.telemetry.serializers import ContainerSerializer

# Create your views here.
def containers(request):
    return HttpResponse("Hello!")

class ContainerViewSet(viewsets.ModelViewSet):
    queryset = Container.objects.all().order_by('-due_at')
    serializer_class = ContainerSerializer