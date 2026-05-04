"""
Entry point para despliegue en Vercel.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

# Crear aplicación WSGI pura
app = get_wsgi_application()

# Handler para Vercel
handler = app
