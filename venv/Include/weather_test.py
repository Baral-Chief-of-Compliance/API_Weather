import requests
import json


def get_weather():

    r = requests.get('https://api.weather.yandex.ru/v2/forecast?lat=68.908513&lon=33.083164&extra=true', headers={"X-Yandex-API-Key": "16c0b05c-66b2-4e79-84d3-0f46907dc28a"})

    with open('data.json', 'w', encoding="utf-8") as file:
        file.write(r.text)

    file.close()

    weather = {}

    with open('data.json', 'r', encoding="utf-8") as file:
        data_from_yandex = json.loads(file.read())

        for key in data_from_yandex:
            if (key == "fact"):
                weather = data_from_yandex[key]

    return weather




