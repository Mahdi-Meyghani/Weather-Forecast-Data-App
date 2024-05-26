import requests

API_KEY = "dd13c0f49106559ca9ac24aa67c5471e"


def get_data(city, forcast_days=1):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"

    response = requests.get(url)
    content = response.json()

    filtered_content = content["list"]
    nr_values = 8 * forcast_days
    filtered_content = filtered_content[:nr_values]

    return filtered_content


if __name__ == "__main__":
    data = get_data("Tokyo", 3)
    print(data)
    print(len(data))