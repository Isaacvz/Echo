from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def logged(request):
    return render(request, 'chat.html')