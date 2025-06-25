from django.shortcuts import render
import requests


def weather_view(request):
    weather_data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '5913ab807806f6275287b894dda4d05b'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data ={
                'city':city,
                'temparature':data['main']['temp'],
                'description':data['weather'][0]['description'],
                'icon':data['weather'][0]['icon'],
            }
        else:
            weather_data['error'] ='city  not found or Please enter city' 
    return render(request, 'weather.html', {'weather_data':weather_data})