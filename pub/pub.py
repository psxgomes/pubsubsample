import os
import json
from google.cloud import pubsub_v1
import http.server
import socketserver

# Configuração do Pub/Sub
project_id = os.getenv("playground-s-11-598888e7")
topic_id = os.getenv("meu-topico")

# Criando cliente para Pub/Sub
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# Função para publicar a mensagem no Pub/Sub
def publish_message(message):
    message_json = json.dumps({"message": message}).encode("utf-8")
    publisher.publish(topic_path, message_json)
    print(f"Mensagem publicada: {message}")

# Handler para o servidor HTTP
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Publicar uma mensagem quando uma requisição GET for recebida
        publish_message("Mensagem de teste do pub.py!")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Mensagem publicada no Pub/Sub!")

# Configurar o servidor HTTP para escutar na porta 8080
PORT = int(os.environ.get('PORT', 8080))

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Servidor Pub/Sub em execução na porta {PORT}")
    httpd.serve_forever()
