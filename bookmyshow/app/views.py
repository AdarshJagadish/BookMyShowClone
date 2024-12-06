from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return request(render,'index.html')

# Create your views here.
