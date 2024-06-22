import logging
from twilio.rest import Client
from fastapi import FastAPI, Request
from app import response
from urllib.parse import parse_qs
from dotenv import dotenv_values

config = dotenv_values(".env")

app = FastAPI()

TWILIO_ACCOUNT_SID = config["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = config["TWILIO_AUTH_TOKEN"]
TWILIO_NUMBER = config["TWILIO_NUMBER"]

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)
twilio_number = TWILIO_NUMBER 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_message(to_number, body_text):
    try:
        message = client.messages.create(
            from_=f"whatsapp:{twilio_number}",
            body=body_text,
            to=f"whatsapp:{to_number}"
        )
        logger.info(f"Message sent to {to_number}: {message.body}")
    except Exception as e:
        logger.error(f"Error sending message to {to_number}: {e}")

@app.post("/")
async def reply(request: Request):
    form_data = parse_qs(await request.body())
    message_body = form_data[b'Body'][0].decode()
    from_number = form_data[b'From'][0].decode().split(':')[1]  # Extrai o número do remetente

    try:
        chat_response = response(message_body)  # Chama a função response
        send_message(from_number, chat_response)  # Envia a resposta para o remetente
    except Exception as e:
        chat_response = "Ocorreu um erro. Por favor, tente novamente mais tarde."
        send_message(from_number, chat_response)
        logger.error(f"Error: {e}")
    return chat_response
