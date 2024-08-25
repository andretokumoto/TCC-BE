# Use uma imagem base com Python 3.12
FROM python:3.12-slim

# Atualize e instale as dependências do sistema necessárias
RUN apt-get update && apt-get install -y texlive-latex-base

# Copie o requirements.txt
COPY requirements.txt /app/requirements.txt

WORKDIR /app

# Instale as dependências usando o pip
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do seu código para o contêiner
COPY . /app/
