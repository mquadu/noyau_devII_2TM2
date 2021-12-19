# Marina
from ..data.config import cine_link
import requests


class Cine:
    def __init__(self, origin='Louvain-la-Neuve'):
        self.__origin = origin
        self.__url_origin = cine_link(self.origin)

    @property
    def url_origin(self):
        return self.__url_origin

    @property
    def origin(self):
        return self.__origin

    @origin.setter
    def origin(self, origin):
        self.__origin = origin

    def get_cine(self):
        """
        PRE : "/cine"
        POST : liste des cinemas du lieu passé en paramètre (par défaut LLN)
        RAISES : exception : si pas de réponse à la requete
        """
        try:
            response = requests.get(self.url_origin).json()
        except ValueError:
            return "Can't fetch Cinema"

        cine = ""
        for i in response:
            cine += f"{i['display_name']}\n"
        return cine


var = [{'place_id': 60799619, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
        'osm_type': 'node', 'osm_id': 5472585695, 'boundingbox': ['50.6691735', '50.6692735', '4.611501', '4.611601'],
        'lat': '50.6692235', 'lon': '4.611551',
        'display_name': 'Parking Grand Place - Entrée piéton (Cinéma), Grand Place, Bruyères, Louvain-la-Neuve, '
                        'Ottignies-Louvain-la-Neuve, Nivelles, Brabant wallon, Wallonie, 1348, België / Belgique / '
                        'Belgien',
        'class': 'amenity', 'type': 'parking_entrance', 'importance': 0.30100000000000005,
        'address': {'amenity': 'Parking Grand Place - Entrée piéton (Cinéma)', 'road': 'Grand Place',
                    'neighbourhood': 'Bruyères', 'town': 'Louvain-la-Neuve', 'county': 'Nivelles',
                    'state': 'Brabant wallon', 'region': 'Wallonie', 'postcode': '1348',
                    'country': 'België / Belgique / Belgien', 'country_code': 'be'}}]

var3 = [{'place_id': 3113491, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
         'osm_type': 'node', 'osm_id': 389938252, 'boundingbox': ['50.7116483', '50.7117483', '4.5209694', '4.5210694'],
         'lat': '50.7116983', 'lon': '4.5210194',
         'display_name': 'Ciné Centre, 91, Avenue de Merode, Fond du Patch, Bourgeois, Rixensart, Nivelles, '
                         'Brabant wallon, Wallonie, 1330, België / Belgique / Belgien',
         'class': 'amenity', 'type': 'cinema', 'importance': 0.11100000000000002,
         'icon': 'https://nominatim.openstreetmap.org/ui/mapicons//tourist_cinema.p.20.png',
         'address': {'amenity': 'Ciné Centre', 'house_number': '91', 'road': 'Avenue de Merode',
                     'neighbourhood': 'Fond du Patch', 'village': 'Bourgeois', 'city': 'Rixensart',
                     'municipality': 'Rixensart', 'county': 'Nivelles', 'state': 'Brabant wallon', 'region': 'Wallonie',
                     'postcode': '1330', 'country': 'België / Belgique / Belgien', 'country_code': 'be'}}]

var_wavre = [
    {'place_id': 118583596, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
     'osm_type': 'way', 'osm_id': 71444739, 'boundingbox': ['50.7001144', '50.7003976', '4.590172', '4.5906048'],
     'lat': '50.7002958', 'lon': '4.590404271098004',
     'display_name': "Cinema 4D, Boulevard de l'Europe, Limal, Wavre, Nivelles, Brabant wallon, Wallonie, 1300, België "
                     "/ Belgique / Belgien",
     'class': 'building', 'type': 'yes', 'importance': 0.21100000000000002,
     'address': {'building': 'Cinema 4D', 'road': "Boulevard de l'Europe", 'village': 'Limal', 'town': 'Wavre',
                 'county': 'Nivelles', 'state': 'Brabant wallon', 'region': 'Wallonie', 'postcode': '1300',
                 'country': 'België / Belgique / Belgien', 'country_code': 'be'}},
    {'place_id': 325329544, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
     'osm_type': 'way', 'osm_id': 139078530, 'boundingbox': ['50.8373959', '50.8378229', '4.3628516', '4.3632022'],
     'lat': '50.83761505', 'lon': '4.363010433724834',
     'display_name': 'Cinéma Vendôme, 18, Chaussée de Wavre - Waverse Steenweg, Matongé, Ixelles - Elsene, Brussel-'
                     'Hoofdstad - Bruxelles-Capitale, Région de Bruxelles-Capitale - Brussels Hoofdstedelijk Gewest, '
                     '1050, België / Belgique / Belgien',
     'class': 'amenity', 'type': 'cinema', 'importance': 0.101,
     'icon': 'https://nominatim.openstreetmap.org/ui/mapicons//tourist_cinema.p.20.png',
     'address': {'amenity': 'Cinéma Vendôme', 'house_number': '18', 'road': 'Chaussée de Wavre - Waverse Steenweg',
                 'neighbourhood': 'Matongé', 'town': 'Ixelles - Elsene',
                 'county': 'Brussel-Hoofdstad - Bruxelles-Capitale',
                 'region': 'Région de Bruxelles-Capitale - Brussels Hoofdstedelijk Gewest', 'postcode': '1050',
                 'country': 'België / Belgique / Belgien', 'country_code': 'be'}}]

var_namur = [
    {'place_id': 222863620, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
     'osm_type': 'way', 'osm_id': 587043433, 'boundingbox': ['50.4658521', '50.4660441', '4.8654973', '4.8663496'],
     'lat': '50.465943100000004', 'lon': '4.865938616016884',
     'display_name': 'Cinéma Eldorado, 40, Rue de Fer, Bomel, Namur, Wallonie, 5000, België / Belgique / Belgien',
     'class': 'building', 'type': 'construction', 'importance': 0.11100000000000002,
     'address': {'building': 'Cinéma Eldorado', 'house_number': '40', 'road': 'Rue de Fer', 'hamlet': 'Bomel',
                 'city_district': 'Namur', 'city': 'Namur', 'county': 'Namur', 'state': 'Namur', 'region': 'Wallonie',
                 'postcode': '5000', 'country': 'België / Belgique / Belgien', 'country_code': 'be'}},
    {'place_id': 226866051, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
     'osm_type': 'way', 'osm_id': 620890440, 'boundingbox': ['50.5633963', '50.5636055', '4.6931304', '4.6936571'],
     'lat': '50.56352605', 'lon': '4.693407769887375',
     'display_name': 'Centre Culturel - Cinéma Royal, 55, Rue du Moulin, Gembloux, Namur, Wallonie, 5030, België / '
                     'Belgique / Belgien',
     'class': 'amenity', 'type': 'arts_centre', 'importance': 0.11100000000000002,
     'icon': 'https://nominatim.openstreetmap.org/ui/mapicons//tourist_art_gallery2.p.20.png',
     'address': {'amenity': 'Centre Culturel - Cinéma Royal', 'house_number': '55', 'road': 'Rue du Moulin',
                 'city_district': 'Gembloux', 'town': 'Gembloux', 'county': 'Namur', 'state': 'Namur',
                 'region': 'Wallonie', 'postcode': '5030', 'country': 'België / Belgique / Belgien',
                 'country_code': 'be'}},
    {'place_id': 226813198, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
     'osm_type': 'way', 'osm_id': 612158412, 'boundingbox': ['49.9786676', '49.9788539', '4.9366562', '4.9369298'],
     'lat': '49.97876125', 'lon': '4.936793421073069',
     'display_name': 'Cinéma de Gedinne, 11, Rue de la Croisette, Gedinne, Dinant, Namur, Wallonie, 5575, België / '
                     'Belgique / Belgien',
     'class': 'amenity', 'type': 'cinema', 'importance': 0.11100000000000002,
     'icon': 'https://nominatim.openstreetmap.org/ui/mapicons//tourist_cinema.p.20.png',
     'address': {'amenity': 'Cinéma de Gedinne', 'house_number': '11', 'road': 'Rue de la Croisette',
                 'village': 'Gedinne', 'county': 'Dinant', 'state': 'Namur', 'region': 'Wallonie', 'postcode': '5575',
                 'country': 'België / Belgique / Belgien', 'country_code': 'be'}}]
