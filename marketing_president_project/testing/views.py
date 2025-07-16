from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def testing_home(request):
    return render(request, 'testing/index.html')
