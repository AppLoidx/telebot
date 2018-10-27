from lilly import Lilly
import requests
import time

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


lilly = Lilly()
while True:
    print(listen(0.5))

