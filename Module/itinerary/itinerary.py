import Module.data.config as config
import requests


class ParameterException(Exception):
    pass


def process_request(lon_o, lat_o, lon_d, lat_d):
    return requests.get(
        config.open_street_link + '&start=' + lon_o + ',' +
        lat_o + '&end=' + lon_d + ',' + lat_d,
        headers=config.headers).json()


class Itinerary:
    def __init__(self, origin_address="Louvain-la-neuve", destination_address=""):
        self.__origin_address = origin_address
        self.__destination_address = destination_address

        self.__url_address_origin = config.itinerary_link(origin_address)

        self.__url_address_destination = config.itinerary_link(destination_address)

    @property
    def url_address_origin(self):
        return self.__url_address_origin

    @property
    def url_address_destination(self):
        return self.__url_address_destination

    def get_itinerary(self):
        response_origin = requests.get(self.url_address_origin).json()
        response_destination = requests.get(self.url_address_destination).json()

        origin_long = response_origin[0]["lon"]
        origin_lat = response_origin[0]["lat"]
        destination_long = response_destination[0]["lon"]
        destination_lat = response_destination[0]["lat"]

        itinerary = process_request(origin_long, origin_lat, destination_long, destination_lat)

        print(itinerary)
        steps = itinerary["features"][0]["properties"]["segments"][0]["steps"]

        print(steps)

        way = ""
        for i in range(len(steps)):
            way += f"etape {i}:"
            way += f"{steps[i]['instruction']} --> Distance : {steps[i]['distance']} m\n\n"
        return way
