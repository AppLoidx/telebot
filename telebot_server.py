import requests
import time

from telebot import Telebot
from message_manager.manager import Message

url = "https://api.telegram.org/bot627640438:AAEMONrxNiMFDVVMWA2e3Ss902tsp748Pgs/"


def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def start():
    pass


def listen(deltatime=0.0):
    time.sleep(deltatime)
    return last_update(get_updates_json(url))


last_update_id = listen()
telebot = Telebot()

while True:
    message = listen(0.5)
    if message != last_update_id:
        response = telebot.cmd_input(Message.get_text(message))
        send_mess(Message.get_chat_id(message), response)
