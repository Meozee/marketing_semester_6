from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

@staff_member_required
def approval_home(request):
    return render(request, 'approval/index.html')
