# Base image
FROM python:3.12-slim

# Atualiza os pacotes e instala dependências do LaTeX
RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-xetex \
    && rm -rf /var/lib/apt/lists/* \
    && pdflatex --version  

# Cria o diretório para arquivos temporários com permissões apropriadas
RUN mkdir -p /app/FormataiBE_API/templates/arquivos_temp && chmod -R 777 /app/FormataiBE_API/templates/arquivos_temp

# Copie o requirements.txt
COPY requirements.txt /app/requirements.txt

WORKDIR /app

# Instale as dependências Python usando o pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Copie o restante do seu código para o contêiner
COPY . /app/

# Inicia o Gunicorn com configuração de workers adequados
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "FormataiBackEnd.wsgi:application"]
