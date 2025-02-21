FROM python:3.9
WORKDIR /app
COPY sub.py requirements.txt ./
RUN pip install -r requirements.txt
# Expor a porta 8080 (port padrão para Cloud Run)
EXPOSE 8080

# Definir variável de ambiente PORT para o Cloud Run
ENV PORT 8080
CMD ["python", "sub.py"]
