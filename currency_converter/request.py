import requests


def take_symbs():
    url = "https://api.exchangerate.host/symbols"
    response = requests.get(url)
    data = response.json()

    result = tuple((symb, symb) for symb in data["symbols"].keys())
    return result


def convert(value, fromCur, toCur):
    url = f"https://api.exchangerate.host/convert?from={fromCur}&to={toCur}&amount={value}"
    response = requests.get(url)
    data = response.json()
    if data["success"]:
        return data["result"]
