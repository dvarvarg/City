from opencage.geocoder import OpenCageGeocode


def get_coordinates(city,key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return 'Город не найден'


key = '31889b09103942fca06007cc1ed29fe1'
city='Moscow'
coordinates=get_coordinates(city,key)
print(f'Координаты города {city}: {coordinates}')

