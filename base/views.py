from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello, this is my first Django page!')

def greeting(request):
    return JsonResponse({'message': 'Hello, welcome to our API!'})