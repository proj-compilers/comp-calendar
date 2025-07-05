#!/bin/bash

echo "Instalando dependências..."
pip install antlr4-python3-runtime
pip install google-api-python-client
pip install google-auth

echo "Entrando na pasta src..."
cd src || { echo "Pasta 'src' não encontrada!"; exit 1; }

echo "Executando o compilador com input.txt..."
python main.py input.txt
