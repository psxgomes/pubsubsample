from google.cloud import pubsub_v1

# Configuração
PROJECT_ID = "playground-s-11-598888e7"
SUBSCRIPTION_ID = "minha-assinatura"

# Inicializa o cliente do Pub/Sub
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

def callback(message):
    print(f"📩 Mensagem recebida: {message.data.decode('utf-8')}")
    message.ack()  # Confirma o recebimento

# Iniciar a escuta
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)

print("🚀 Ouvindo mensagens...")
try:
    streaming_pull_future.result()
except KeyboardInterrupt:
    streaming_pull_future.cancel()
