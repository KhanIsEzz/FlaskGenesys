from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'EVAHUB/index.html', context={})
# Create your views here.
