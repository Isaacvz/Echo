from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import traceback
from main.views import logged

@csrf_exempt
def login_ajax(request):
    if request.method == "POST":
        try:
            # Verificar Content-Type
            content_type = request.headers.get('Content-Type', '')
            
            # Debug: imprimir información del request
            print(f"[DEBUG] Content-Type: {content_type}")
            print(f"[DEBUG] Request body: {request.body}")
            print(f"[DEBUG] Request POST: {request.POST}")
            
            # Si el body está vacío, devolver error
            if not request.body:
                return JsonResponse({"status": "error", "message": "Request body vacío"}, status=400)
            
            # Intentar parsear JSON
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError as json_error:
                print(f"[ERROR] JSON decode error: {str(json_error)}")
                print(f"[ERROR] Body recibido: {request.body.decode('utf-8', errors='replace')}")
                return JsonResponse({"status": "error", "message": f"JSON inválido: {str(json_error)}"}, status=400)
            
            username = data.get('username')
            password = data.get('password')
            
            print(f"[DEBUG] Username recibido: {username}")
            print(f"[DEBUG] Password recibido: {'Si' if password else 'No'}")

            # Verificamos credenciales en la DB
            user = authenticate(request, username=username, password=password)
            print(f"[DEBUG] Resultado authenticate: {user}")

            if user is not None:
                login(request, user) # Crea la sesión en el servidor
                print(f"[DEBUG] Login exitoso para: {username}")
                return JsonResponse({"status": "success", "redirect": "/chat/"})
            else:
                print(f"[DEBUG] Autenticación fallida para: {username}")
                return JsonResponse({"status": "error", "message": "Usuario o contraseña incorrectos"}, status=401)
                
        except Exception as e:
            error_traceback = traceback.format_exc()
            print(f"[ERROR] Excepción en login_ajax: {str(e)}")
            print(f"[ERROR] Traceback: {error_traceback}")
            return JsonResponse({"status": "error", "message": str(e), "traceback": error_traceback}, status=500)
            
    print(f"[DEBUG] Método no permitido: {request.method}")
    return JsonResponse({"status": "error", "message": "Método no permitido"}, status=405)