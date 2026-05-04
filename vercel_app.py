"""
Entry point para despliegue en Vercel.
"""
import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

# Crear aplicación WSGI
application = get_wsgi_application()

# Wrap con WhiteNoise para servir archivos estáticos
app = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), 'staticfiles'))

# Handler para Vercel
handler = app
