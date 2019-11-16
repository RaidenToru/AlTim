from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def personal(request):
    return render(request, 'personalPage.html')
