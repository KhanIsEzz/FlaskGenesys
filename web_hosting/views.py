from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Wow! Writing First Web App In Django!")
# Create your views here.
