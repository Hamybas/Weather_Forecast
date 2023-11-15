import requests

APIkey = "7da60fbd1a95f8edc9bbbb4f0b92358e"


def get_data(place, forecast_days, kind):
    url = (f"https://api.openweathermap.org/data/2.5/"
           f"forecast?q={place}&"
           f"appid={APIkey}")
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == 'Temperature':
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if kind == 'Sky':
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data('Tokyo', 4, 'Temperature'))
