#!/bin/bash
# Script para construir archivos estáticos antes del despliegue

echo "Building project..."

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Aplicar migraciones (opcional, para base de datos SQLite)
python manage.py migrate

echo "Build completed!"
