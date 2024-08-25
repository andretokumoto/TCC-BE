# Use uma imagem base com Python 3.12
FROM python:3.12-slim

# Atualize e instale pipenv
RUN apt-get update && apt-get install -y pipenv

# Instale as dependências do sistema necessárias (opcional)
RUN apt-get install -y texlive-latex-base

# Copie o Pipfile e o Pipfile.lock
COPY Pipfile Pipfile.lock /app/

WORKDIR /app

# Instale as dependências usando o Pipenv
RUN pipenv install --deploy --ignore-pipfile

# Copie o restante do seu código para o contêiner
COPY . /app/
