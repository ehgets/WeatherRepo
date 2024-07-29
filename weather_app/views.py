from django.shortcuts import render

import requests
from django.shortcuts import render
from django.conf import settings


def get_weather(request):
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.POST.get('city')
        country = request.POST.get('country')
        api_key = settings.OPEN_WEATHER_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'description': data['weather'][0]['description'],
            }
        else:
            error = 'City not found or invalid API key.'

    return render(request, 'weather/weather.html', {'weather_data': weather_data, 'error': error})

