import requests

API_KEY = "dd13c0f49106559ca9ac24aa67c5471e"


def get_data(city, forcast_days=1, kind="Temperature"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"

    response = requests.get(url)
    content = response.json()


    return content


if __name__ == "__main__":
    data = get_data("Tokyo", 3, "Sky")
    print(data)
    print(len(data))