from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def first_page(request):
    return render(request, 'base/first_page.html')

def greeting(request):
    return JsonResponse({'message': 'Hello, welcome to our API!'})