from google.cloud import pubsub_v1

# Configuração
PROJECT_ID = "playground-s-11-598888e7"
TOPIC_ID = "meu-topico"

# Inicializa o cliente do Pub/Sub
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

def publicar_mensagem(mensagem):
    future = publisher.publish(topic_path, mensagem.encode("utf-8"))
    print(f"📨 Mensagem enviada: {mensagem}, ID: {future.result()}")

# Enviar uma mensagem
if __name__ == "__main__":
    publicar_mensagem("Olá, mundo do Pub/Sub!")
