from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

@staff_member_required
def admin_panel(request):
    return render(request, 'adminpanel/index.html')
