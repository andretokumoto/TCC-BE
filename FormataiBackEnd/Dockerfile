# Base image
FROM python:3.12-slim

# Atualiza os pacotes e instala dependências do LaTeX
RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-latex-base \        
    texlive-latex-extra \       
    texlive-fonts-recommended \ 
    texlive-xetex \             
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . /app

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta (se necessário para o Django)
EXPOSE 8000

# Comando de inicialização
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
