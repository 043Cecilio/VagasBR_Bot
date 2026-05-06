import os
import requests

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

def buscar_vagas():
  
    return [
        {"titulo": "Estágio em Tecnologia", "link": "https://www.linkedin.com/jobs/"},
        {"titulo": "Estágio em Administração", "link": "https://www.ciee.org.br/"}
    ]

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": texto, "parse_mode": "Markdown"}
    requests.post(url, data=data)

if __name__ == "__main__":
    vagas = buscar_vagas()
    for vaga in vagas:
        msg = f"📢 *Nova vaga encontrada!*\n\n📌 *Cargo:* {vaga['titulo']}\n🔗 [Ver vaga]({vaga['link']})"
        enviar_mensagem(msg)
