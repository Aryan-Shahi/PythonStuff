import requests  
from datetime import datetime

user_api = '---------------'
location = input("Enter city name: ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()  #storing in json format


if api_data['cod'] == "404":
    print ("Invalid city:{}, Please check your city name". format(location))
else:
    temp_city = ((api_data['main']['temp'])-273.15)
    weather_desc = api_data['weather'][0]["description"]
    hmdt = api_data['main']["humidity"]
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    
    print("----------------------------------")
    print("Weather stats for - {} || {}".format(location.upper(), date_time))
    print("Current temperature is: {:.2f} deg C".format(temp_city))
    print("current weatehr desc: ", weather_desc)
    print("Current Humidity:",hmdt, '%')
    print("Current wind speed: ",wind_spd, 'kmph')
