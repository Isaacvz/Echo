from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_ajax, name='login_ajax')
]