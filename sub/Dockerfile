# Use a imagem base oficial do Python
FROM python:3.9-slim

# Definir diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos do projeto para o container
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir google-cloud-pubsub

# Expor a porta 8080
EXPOSE 8080

# Definir variável de ambiente PORT para o Cloud Run
ENV PORT 8080

# Comando para iniciar o serviço (pub.py ou sub.py)
CMD ["python", "sub.py"]  # Altere para sub.py quando necessário
