from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def login_view(request):
    return render(request, 'login.html')

@login_required
def logged(request):
    return render(request, 'chat.html')