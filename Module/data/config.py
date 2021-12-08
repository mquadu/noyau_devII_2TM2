import sys
import os

# Link open street service
headers = {'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8', }
open_street_link = 'https://api.openrouteservice.org/v2/directions/driving-car?api_key' \
                   '=5b3ce3597851110001cf62481288a0a3b2fe4b43a2d8a701aaaa3436 '

# Directory containing
ROOT_DIR = "\\".join(sys.path[0].split('\\')[:-1])

MODULE_DIR = os.path.join(ROOT_DIR, "Module")
HELP_FILE = os.path.join(MODULE_DIR, "data\help.txt")
CERTIFICATE_FILE = os.path.join(MODULE_DIR, "data\\2TM2-G2.pem")


# Link nominatim openstreetmap
def itinerary_link(address):
    return 'https://nominatim.openstreetmap.org/search/' + address + '?format=json'


def weather_stack(param):
    return f"http://api.weatherstack.com/current?access_key=4c53b8fcf4818536539b668a0247408c&query={param}"


def cine_link(address):
    return f"https://nominatim.openstreetmap.org/search?osmtype=N&addressdetails=1&q=cinema+{address}&format=json"


def resto_link(address):
    return f"https://nominatim.openstreetmap.org/search?osmtype=N&addressdetails=1&q=restaurant+{address}&format=json"
