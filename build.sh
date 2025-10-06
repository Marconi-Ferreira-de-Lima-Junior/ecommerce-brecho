#!/bin/bash
echo "🚀 Iniciando build do projeto Django"

# Instala dependências
pip install -r requirements.txt

# Aplica migrações do banco
python manage.py migrate --noinput

# Coleta os arquivos estáticos
python manage.py collectstatic --noinput

echo "✅ Build finalizado com sucesso!"
