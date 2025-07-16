from django.shortcuts import render

def homepage(request):
    return render(request, 'core/homepage.html')

def about(request):
    return render(request, 'core/about.html')
