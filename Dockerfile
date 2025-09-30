# Imagem base oficial do Python
FROM python:3.13-slim-bookworm

# Evita que o Python guarde cache
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Diretório de 
# Nossa app principal já se chama /app
WORKDIR /code

# Instalar dependências
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código do projeto
COPY . /code/

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]