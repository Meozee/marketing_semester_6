from django.shortcuts import render

def dashboard_home(request):
    return render(request, 'dashboard/national.html')  # nanti kita buat file ini
