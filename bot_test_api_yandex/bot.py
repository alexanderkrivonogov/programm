import requests
from pprint import pprint
import telebot

bot = telebot.TeleBot("")


def get_address_from_coords(coords):
    PARAMS = {
        "apikey": "",
        "format": "json",
        "lang": "ru_RU",
        "kind": "house",
        "geocode": coords,

    }

    try:
        r = requests.get(url="https://geocode-maps.yandex.ru/1.x/", params=PARAMS)
        # получаем данные
        json_data = r.json()
        # вытаскиваем из всего пришедшего json именно строку с полным адресом.
        address_str = json_data["response"]["GeoObjectCollection"]["featureMember"][0]['GeoObject']['Point']['pos']
        # возвращаем полученный адрес
        return address_str
    except Exception as e:
        # если не смогли, то возвращаем ошибку
        return "error"


@bot.message_handler(commands=["start"])
def unknown_message(message):
    bot.send_location(message.chat.id, adress_str.split()[-1], adress_str.split()[-2])


if __name__ == "__main__":
    adress_str = get_address_from_coords("Сургут 30 лет победы 60/1")
    pprint(adress_str.split()[::-1])

    bot.polling()
