from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import json

def login_ajax(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            # Verificamos credenciales en la DB
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user) # Crea la sesión en el servidor
                return JsonResponse({"status": "success", "message": "¡Bienvenido!"})
            else:
                return JsonResponse({"status": "error", "message": "Usuario o contraseña incorrectos"}, status=401)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
            
    return JsonResponse({"status": "error", "message": "Método no permitido"}, status=405)