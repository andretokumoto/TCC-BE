# Use uma imagem base com Python e LaTeX
FROM python:3.11-slim

# Instale o pdflatex
RUN apt-get update && apt-get install -y texlive-latex-base

# Configure o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY . .

# Instale as dependências do Python
RUN pip install -r requirements.txt

# Comando para iniciar a aplicação
CMD ["pipenv", "run", "gunicorn", "FormataiBackEnd.wsgi"]
