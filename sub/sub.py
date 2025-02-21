import os
import json
from google.cloud import pubsub_v1
import http.server
import socketserver

# Configuração do Pub/Sub
project_id = os.getenv("playground-s-11-598888e7")
subscription_id = os.getenv("minha-assinatura")

# Criando cliente para Pub/Sub
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

# Função para processar a mensagem recebida
def callback(message):
    print(f"Mensagem recebida: {message.data.decode('utf-8')}")
    message.ack()

# Configurar o servidor HTTP para escutar na porta 8080
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Iniciar o pull de mensagens do Pub/Sub quando o serviço for acessado
        streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
        print(f"Iniciando assinatura do Pub/Sub na subscrição: {subscription_id}")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("Assinante Pub/Sub está ativo!")

# Configurar o servidor HTTP para escutar na porta 8080
PORT = int(os.environ.get('PORT', 8080))

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Servidor Pub/Sub em execução na porta {PORT}")
    httpd.serve_forever()
