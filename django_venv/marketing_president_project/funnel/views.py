from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def funnel_home(request):
    return render(request, 'funnel/index.html')
