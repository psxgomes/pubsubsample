FROM python:3.9
WORKDIR /app
COPY publicador.py requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "publicador.py"]
