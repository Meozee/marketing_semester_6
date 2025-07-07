from django.http import HttpResponse

def testing_home(request):
    return HttpResponse("Halaman Data Testing")
