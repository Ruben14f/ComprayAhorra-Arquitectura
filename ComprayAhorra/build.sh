#!/usr/bin/env bash

set -o errexit  # Termina el script si algún comando falla

# Instalar las dependencias del proyecto
pip install -r requirements.txt

# Recopilar archivos estáticos para producción
python ComprayAhorra/manage.py collectstatic --noinput

# Aplicar las migraciones de base de datos
python ComprayAhorra/manage.py migrate
