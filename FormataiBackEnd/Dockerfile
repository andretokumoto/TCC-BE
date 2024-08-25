FROM python:3.11

# Crie um diretório de trabalho
WORKDIR /app

# Instale as dependências do sistema necessárias (por exemplo, LaTeX)
RUN apt-get update && apt-get install -y texlive-latex-base

# Copie o Pipfile e o Pipfile.lock para o contêiner
COPY Pipfile Pipfile.lock ./

# Instale o Pipenv
RUN pip install pipenv

# Instale as dependências usando o Pipenv
RUN pipenv install --deploy --ignore-pipfile

# Copie o restante do seu código para o contêiner
COPY . .

# Comando para iniciar seu aplicativo (usando o Pipenv)
CMD ["pipenv", "run", "gunicorn", "FormataiBackEnd.wsgi:application", "--bind", "0.0.0.0:8000"]
