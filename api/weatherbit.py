import requests

CITY_ID = {"SPb": 498817, "Ykt": 2013159, "Novosibirsk": 1496747}
BASE_URL = "https://api.weatherbit.io/v2.0/current"
FORECAST_BASE_URL ="https://api.weatherbit.io/v2.0/forecast/3hourly"
response = requests.get(BASE_URL+"")
key = "0a2347ffc1e249b691009558218ec9d3"


def get_weather(city_id, lunguage="ru"):
    req = f"{BASE_URL}?city_id={city_id}&lang={lunguage}&key={key}"
    return requests.get(req).json()


def get_forecast_weather(city_id, lunguage="ru"):
    req = f"{FORECAST_BASE_URL}?city_id={city_id}&lang={lunguage}&key={key}"
    return requests.get(req).json()


f = get_forecast_weather(CITY_ID["SPb"])
print(f)