# Link open street service
headers = {'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8', }
open_street_link = 'https://api.openrouteservice.org/v2/directions/driving-car?api_key' \
                   '=5b3ce3597851110001cf62481288a0a3b2fe4b43a2d8a701aaaa3436 '


# Link nominatim openstreetmap
def nominatim_link(address):
    return 'https://nominatim.openstreetmap.org/search/' + address + '?format=json'
