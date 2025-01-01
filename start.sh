#!/bin/bash

# Navegue até o diretório do projeto
cd /Dcoder/Django_carros/

# AtC:\Dcoder\Django_carros ivar o ambiente virtual
source venv/bin/activate

# Iniciar o servidor
python manage.py runserver 0.0.0.0:8000

echo "Servidor Django rodando em http://0.0.0.0:8000/"