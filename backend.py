import requests

API_KEY = "dd13c0f49106559ca9ac24aa67c5471e"


def get_data(city, forcast_days=1, kind="Temperature"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"

    response = requests.get(url)
    content = response.json()

    filtered_content = content["list"]
    nr_values = 8 * forcast_days
    filtered_content = filtered_content[:nr_values]

    if kind == "Temperature":
        filtered_content = [value["main"]["temp"] for value in filtered_content]

    if kind == "Sky":
        filtered_content = [value["weather"][0]["main"] for value in filtered_content]

    return filtered_content


if __name__ == "__main__":
    data = get_data("Tokyo", 3, "Sky")
    print(data)
    print(len(data))