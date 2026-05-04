"""
Entry point para despliegue en Vercel.
Vercel usa serverless functions que no soportan WebSockets directamente.
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

# Crear aplicación ASGI para Vercel
app = get_asgi_application()

# Handler para Vercel
handler = app
