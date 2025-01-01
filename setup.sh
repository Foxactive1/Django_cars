#!/bin/bash

# Navegue até o diretório do projeto
cd Dcoder/Django_carros/

# Criar ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate

# Instalar Django
pip install django

# Criar o projeto Django
django-admin startproject Django_carros .

# Criar o aplicativo de carros
python manage.py startapp cars

# Instalar Pillow para upload de imagens
pip install Pillow

# Criar as migrações iniciais
python manage.py makemigrations cars
python manage.py migrate

echo "Configuração completa. Para ativar o ambiente, use: source venv/bin/activate"