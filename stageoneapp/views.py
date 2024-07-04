import requests
from django.http import JsonResponse
from django.views import View
from django.conf import settings

class HelloView(View):
    def get(self, request):
        visitor_name = request.GET.get('visitor_name', 'Visitor')
        client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
        
        geo_response = requests.get(f'https://ipapi.co/{client_ip}/json/')
        geo_data = geo_response.json()
        city = geo_data.get('city', 'New York')

        weather_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={settings.WEATHER_API_KEY}')
        weather_data = weather_response.json()
        temperature = weather_data['main']['temp']
        
        greeting = f'Hello, {visitor_name}!, the temperature is {temperature} degrees Celcius in {city}'
        
        response_data = {
            'client_ip': client_ip,
            'location': city,
            'greeting': greeting
        }
        
        return JsonResponse(response_data)

