import requests

appid = "a37f2135c52e78af5aa14f62638ab523"
url = "http://api.weatherstack.com/current?access_key={}&query={}"


def check(res: dict) -> bool:
    return False in res.values()


def second_data(city_name: str) -> str or dict:
    res = requests.get(url.format(appid, city_name)).json()
    if check(res):
        return "city not found"
    else:
        city_info = {
            "city": city_name,
            "temp": f'{res["current"]["temperature"]} C',
            "temp_feels": f'{res["current"]["feelslike"]} C',
            "weather": "".join(res["current"]["weather_descriptions"]),
            "pressure": f'{res["current"]["pressure"]} Pa',
            "humidity": f'{res["current"]["humidity"]} %',
            "visibility": f'{res["current"]["visibility"]} km',
            "speed_wind": f'{int(res["current"]["wind_speed"] / 3.6)} m/c',
        }
    return city_info
