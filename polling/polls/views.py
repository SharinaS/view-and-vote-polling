from django.shortcuts import render
from django.http import HttpResponse

# Views
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
