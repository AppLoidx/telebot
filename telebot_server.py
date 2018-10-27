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


def start():
    pass


def listen(deltatime):
    time.sleep(deltatime)
    return last_update(get_updates_json(url))


telebot = Telebot()

while True:
    last_update_id = None
    message = listen(0.5)
    if message != last_update_id:
        telebot.cmd_input(Message.get_text(message))
    else:
        pass