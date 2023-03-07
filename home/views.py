from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from home.models import *


# Create your views here.

def index(request):
    # Page from the theme
    return render(request, 'pages/index.html')

