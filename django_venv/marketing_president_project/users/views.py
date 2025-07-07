from django.http import HttpResponse

def profile(request):
    return HttpResponse("Halaman Profil Pengguna")

def logout_view(request):
    return HttpResponse("Logout Berhasil (dummy)")
