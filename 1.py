import requests


def take_symbs():
    url = "https://api.exchangerate.host/symbols"
    response = requests.get(url)
    data = response.json()

    result = tuple((symb, symb) for symb in data["symbols"].keys())
    return result
