import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass


load_dotenv
api_key=os.getenv('API_KEY')

@dataclass
class WeatherData:
    main:str
    description: str
    icon: str
    tempreture: float
    min_tempreture: float
    max_tempreture: float
    air_pressure: int
    humidity: int
    


def get_lang_long(city_name, state_code, country_code, API_key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
   
    data = response[0]
    lat, lon =data.get('lat'), data.get('lon')
    return lat, lon

    #print(response)

#get_lang_long('Dublin','Leinster','Ireland', api_key)


def get_current_weather(lat, lon, API_key):
    response= requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
   
    data= WeatherData(
        main=response.get('weather')[0].get('main'),
        description=response.get('weather')[0].get('description'),
        icon=response.get('weather')[0].get('icon'),
        tempreture=response.get('main').get('temp'),
        min_tempreture=response.get('main').get('temp_min'),
        max_tempreture=response.get('main').get('temp_max'),
        air_pressure=response.get('main').get('pressure'),
        humidity=response.get('main').get('humidity')

        )
    
    return data


if __name__=="__main__":
    lat ,lon = get_lang_long('Dublin','Leinster', 'Ireland', api_key)

    print(get_current_weather(lat, lon, api_key))





#print(get_lang_long('Dublin','Leinster', 'Ireland', api_key))        
