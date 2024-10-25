from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser
import requests


def get_coord(key,city):
    global lat, lng
    try:
        geokey = OpenCageGeocode(key)  # обратились к сайту, чтоб получить информацию
        result = geokey.geocode(city, language='ru')
        if result:
            lat=round(result[0]['geometry']['lat'],2)
            lng=round(result[0]['geometry']['lng'],2)
            map_url=f'https://www.openstreetmap.org/?mlat={lat}&mlon={lng}'
            country=result[0]['components']['country']
            if 'state' in result[0]['components']:
                state = result[0]['components']['state']
                return {'coordinates': f'Страна: {country}, Область: {state} - Широта: {lat} Долгота: {lng}',
                        'map': map_url}
            else:
                return {'coordinates': f'Страна: {country} - Широта: {lat} Долгота: {lng}',
                        'map': map_url}

        else:
            return 'Город не найден'
    except Exception as e:
        return f'Ошибка: {e}'


def show_info(event=None):
    global map
    city_data=city_name.get()
    city_name.delete(0,END)
    result = get_coord(key, city_data)
    info_city.config(text=result['coordinates'])
    map=result['map']


def show_map():
    if map:
        webbrowser.open(map)


def get_weather(lat,lng):
    answer=requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&current_weather=true')
    weather_json=answer.json()
    weather_city=weather_json['current_weather']
    return weather_city


def show_weather():
    weather_city=get_weather(lat, lng)
    info_weather.config(text=f'Градусы: {weather_city['temperature']}')



map=''
lat=''
lng=''


window=Tk()
#window.title('')
#window.geometry()

key='31889b09103942fca06007cc1ed29fe1'

t_m=Label(window,text='Введите название города:', font=('Arial',16))
t_m.pack(pady=5)

city_name=Entry(window,font=('Arial',16))
city_name.pack(pady=5)
city_name.bind('<Return>',show_info)

btn=Button(window,text='Поиск', command=show_info, font=('Arial',16))
btn.pack(pady=5)

info_city=Label(window, font=('Arial',16))
info_city.pack(pady=5)

btn_map=Button(window, text='Посмотреть карту',command=show_map,font=('Arial',16))
btn_map.pack(pady=5)

btn_weather=Button(window, text='Посмотреть погоду',command=show_weather,font=('Arial',16))
btn_weather.pack(pady=5)

info_weather=Label(window, font=('Arial',16))
info_weather.pack(pady=5)

#with open('info_city.json','w') as f:
#    json.dump(result,f,indent=4)

window.mainloop()
