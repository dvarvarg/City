from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser
from tkinter import messagebox as mb


def get_coordinates(city,key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city,language='ru')
        if results:
            lat=round(results[0]['geometry']['lat'],2)
            lon=round(results[0]['geometry']['lng'],2)
            country=results[0]['components']['country']
            local_currency = results[0]['annotations']['currency']['name']
            osm_url=f'https://www.openstreetmap.org/?mlat={lat}&mlon={lon}'

            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return {
                    'coordinates': f'Широта: {lat}, Долгота: {lon}\nСтрана: {country}.\nРегион: {region}\nМестная валюта: {local_currency}',
                    'map_url': osm_url
                        }
            else:
                return {
                    'coordinates': f'Широта: {lat}, Долгота: {lon}\nСтрана: {country}.\nМестная валюта: {local_currency}',
                    'map_url': osm_url
                        }
        else:
            mb.showerror('Ошибка',f'Город "{city}" не найден')
    except Exception as e:
        return f'Возникла ошибка {e}'


def show_coordinates(event=None):
    global map_url
    city=entry.get()
    result = get_coordinates(city, key)
    label.config(text=f'Координаты города {city}:\n {result['coordinates']}')
    map_url=result['map_url']


def show_map():
    if map_url:
        webbrowser.open(map_url)

def clear_entry():
    entry.delete(0,END)
    label.config(text='')


key = '31889b09103942fca06007cc1ed29fe1'
map_url=''

window=Tk()
window.title('Координаты городов')
window.geometry('320x220')

entry=Entry()
entry.pack(pady=5)
entry.bind('<Return>', show_coordinates)

button=Button(window, text='Поиск координат', command=show_coordinates)
button.pack(pady=5)

label=Label(text='Введите город и нажмите на кнопку')
label.pack()

frame=Frame(window)
frame.pack(side=BOTTOM)

map_button=Button(frame, text='Показать карту', command=show_map)
map_button.pack(pady=5)

clear_button=Button(frame, text='Очистить', command=clear_entry)
clear_button.pack(pady=5)

window.mainloop()
