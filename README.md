# Echo Chat - Django + Channels

Aplicación de chat en tiempo real usando Django, Django Channels y WebSockets.

## Características

- Autenticación de usuarios
- Chat en tiempo real con WebSockets
- Interfaz moderna y responsive
- Mensajes diferenciados (azul para míos, gris para otros)

## Requisitos

- Python 3.10+
- Django 6.0+
- Channels 4.0+
- Daphne 4.0+

## Instalación Local

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

## Despliegue en Vercel

### ⚠️ Importante sobre WebSockets

**Vercel NO soporta WebSockets** en su plataforma serverless. Los WebSockets requieren conexiones persistentes que no son compatibles con funciones serverless.

Para desplegar la parte HTTP de la aplicación en Vercel:

1. **Instalar Vercel CLI:**
```bash
npm install -g vercel
```

2. **Configurar variables de entorno en Vercel:**
   - Ve a tu proyecto en Vercel Dashboard
   - Settings → Environment Variables
   - Agrega: `DJANGO_SETTINGS_MODULE` = `main.settings`
   - Agrega: `SECRET_KEY` = `(genera una nueva clave segura)`

3. **Desplegar:**
```bash
vercel
```

### Alternativas para WebSockets en producción

Para tener chat en tiempo real en producción, considera estas alternativas a Vercel:

#### Opción 1: Railway (Recomendado)
```bash
# Instalar Railway CLI
npm install -g @railway/cli

# Login y desplegar
railway login
railway init
railway up
```

#### Opción 2: Render
- Crea un Web Service en Render
- Usa el comando de inicio: `daphne -b 0.0.0.0 -p $PORT main.asgi:application`

#### Opción 3: Fly.io
```bash
# Instalar Fly CLI
curl -L https://fly.io/install.sh | sh

# Desplegar
fly launch
fly deploy
```

#### Opción 4: Usar Pusher/Ably con Vercel
Si necesitas quedarte en Vercel, puedes usar un servicio de WebSockets como Pusher o Ably:

1. Regístrate en [Pusher](https://pusher.com) o [Ably](https://ably.com)
2. Modifica el consumer para usar el servicio externo
3. El frontend se conecta al servicio de Pusher/Ably

## Estructura del Proyecto

```
Echo/
├── main/
│   ├── aut/              # App de autenticación
│   ├── chat/             # App del chat
│   ├── static/           # Archivos estáticos (CSS, JS)
│   ├── templates/        # Templates HTML
│   ├── settings.py       # Configuración Django
│   ├── urls.py           # URLs principales
│   ├── asgi.py           # Configuración ASGI
│   └── wsgi.py           # Configuración WSGI
├── manage.py
├── requirements.txt      # Dependencias
├── vercel.json          # Configuración Vercel
└── README.md
```

## Configuración de Variables de Entorno

Para producción, configura estas variables:

```bash
DEBUG=False
SECRET_KEY=tu-clave-secreta-generada
ALLOWED_HOSTS=tu-dominio.com
DATABASE_URL=url-de-base-de-datos
```

## Generar nueva SECRET_KEY

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Licencia

MIT License
