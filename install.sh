#!/bin/bash

# Crear el entorno virtual
python3 -m venv mi_entorno

# Activar el entorno virtual
source mi_entorno/bin/activate

# Instalar las librerías desde requirements.txt
pip3 install -r requirements.txt