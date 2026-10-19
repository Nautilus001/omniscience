from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def containers(request):
    return HttpResponse("Hello!")