import requests

appid = "6d62ff0c351e1e408a189d47c7bf7b79"
url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid


def check(res: dict) -> bool:
    return "city not found" in res.values()


def first_data(city_name: str) -> str or dict:
    res = requests.get(url.format(city_name)).json()
    if check(res):
        return "city not found"
    else:
        city_info = {
            "city": city_name,
            "temp": f'{round(res["main"]["temp"])} C',
            "temp_feels": f'{round(res["main"]["feels_like"])} C',
            "weather": f'{res["weather"][0]["main"]}',
            "pressure": f'{res["main"]["pressure"]} Pa',
            "humidity": f'{res["main"]["humidity"]} %',
            "visibility": f'{int(res["visibility"] / 1000)} km',
            "speed_wind": f'{int(res["wind"]["speed"])} m/c',
        }
    return city_info
