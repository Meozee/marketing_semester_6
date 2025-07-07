from django.http import HttpResponse

def admin_navbar(request):
    return HttpResponse("Halaman Admin Navbar")

def admin_panel(request):
    return HttpResponse("Halaman Admin Panel (CRUD & Log)")
