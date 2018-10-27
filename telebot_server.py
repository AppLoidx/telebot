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


def listen(deltatime=0.0):
    time.sleep(deltatime)
    return last_update(get_updates_json(url))


def get_last_update_id():
    return Message.get_update_id(listen())


def start():
    last_update_id = get_last_update_id()
    telebot = Telebot()

    while True:
        message = Message(listen(0.5))
        if message.update_id != last_update_id:
            response = telebot.cmd_input(message.text)
            send_mess(message.chat_id, response)
            last_update_id = get_last_update_id()





