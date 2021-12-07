# from OSMPythonTools.nominatim import Nominatim

# import pyroutelib2.route as route
# import urllib.parse
import Module.data.config as config
import requests


# import folium
# import openrouteservice


class Itinerary:
    def __init__(self, origin_address="Louvain-la-neuve", destination_address=""):
        self.__origin_address = origin_address
        self.__destination_address = destination_address

        self.__url_address_origin = config.nominatim_link(origin_address)
        self.__url_address_destination = config.nominatim_link(destination_address)

        self.get_intinerary()

    def get_intinerary(self):
        response_origin = requests.get(self.__url_address_origin).json()
        response_destination = requests.get(self.__url_address_destination).json()

        origin_long = response_origin[0]["lon"]
        origin_lat = response_origin[0]["lat"]
        destination_long = response_destination[0]["lon"]
        destination_lat = response_destination[0]["lat"]

        call = requests.get(
            config.open_street_link + '&start=' + origin_long + ',' +
            origin_lat + '&end=' + destination_long + ',' + destination_lat,
            headers=config.headers)

        # print(call.text)
        obj = call.json()
        # print(obj)

        distance_general = obj["features"][0]["properties"]["segments"][0]["distance"]

        steps = obj["features"][0]["properties"]["segments"][0]["steps"]
        # print(obj["features"][0]["properties"]["segments"][0]) #["properties"]["segments"]["distance"]
        i = 0
        for i in range(len(steps)):
            print(f"etape {i} :")

            print("{0}\nDistance : {1} m\n".format(steps[i]["instruction"], steps[i]["distance"]))


# Format de reponse de openstreet map


# Response openstreetservice

var = {"type": "FeatureCollection", "features": [{"bbox": [4.605783, 50.667945, 4.630322, 50.716361], "type": "Feature",
                                                  "properties": {"segments": [{"distance": 6629.6, "duration": 607.5,
                                                                               "steps": [
                                                                                   {"distance": 275.7, "duration": 63.8,
                                                                                    "type": 11,
                                                                                    "instruction": "Head south on Anneau Central-Sud",
                                                                                    "name": "Anneau Central-Sud",
                                                                                    "way_points": [0, 24]},
                                                                                   {"distance": 437.2, "duration": 66.8,
                                                                                    "type": 13,
                                                                                    "instruction": "Keep right onto Boulevard de Wallonie-Sud",
                                                                                    "name": "Boulevard de Wallonie-Sud",
                                                                                    "way_points": [24, 40]},
                                                                                   {"distance": 434.9, "duration": 39.1,
                                                                                    "type": 13,
                                                                                    "instruction": "Keep right onto Boulevard de Wallonie",
                                                                                    "name": "Boulevard de Wallonie",
                                                                                    "way_points": [40, 55]},
                                                                                   {"distance": 356.5, "duration": 69.1,
                                                                                    "type": 7,
                                                                                    "instruction": "Enter the roundabout and take the 3rd exit onto Boulevard du Brabant Wallon",
                                                                                    "name": "Boulevard du Brabant Wallon",
                                                                                    "exit_number": 3,
                                                                                    "way_points": [55, 76]},
                                                                                   {"distance": 4010.6,
                                                                                    "duration": 173.1, "type": 6,
                                                                                    "instruction": "Continue straight onto Boulevard du Brabant Wallon",
                                                                                    "name": "Boulevard du Brabant Wallon",
                                                                                    "way_points": [76, 118]},
                                                                                   {"distance": 395.3, "duration": 45.5,
                                                                                    "type": 1,
                                                                                    "instruction": "Turn right",
                                                                                    "name": "-",
                                                                                    "way_points": [118, 138]},
                                                                                   {"distance": 172.5, "duration": 30.7,
                                                                                    "type": 7,
                                                                                    "instruction": "Enter the roundabout and take the 2nd exit onto Boulevard de l'Europe, N238",
                                                                                    "name": "Boulevard de l'Europe, N238",
                                                                                    "exit_number": 2,
                                                                                    "way_points": [138, 154]},
                                                                                   {"distance": 46.4, "duration": 13.2,
                                                                                    "type": 5,
                                                                                    "instruction": "Turn slight right onto Boulevard de l'Europe, N238",
                                                                                    "name": "Boulevard de l'Europe, N238",
                                                                                    "way_points": [154, 156]},
                                                                                   {"distance": 26.4, "duration": 6.3,
                                                                                    "type": 0,
                                                                                    "instruction": "Turn left onto Rue du Pont Saint Jean",
                                                                                    "name": "Rue du Pont Saint Jean",
                                                                                    "way_points": [156, 159]},
                                                                                   {"distance": 175.1, "duration": 28.1,
                                                                                    "type": 1,
                                                                                    "instruction": "Turn right onto Rue du Pont Saint Jean",
                                                                                    "name": "Rue du Pont Saint Jean",
                                                                                    "way_points": [159, 172]},
                                                                                   {"distance": 283.5, "duration": 68.0,
                                                                                    "type": 1,
                                                                                    "instruction": "Turn right onto Rue de Nivelles",
                                                                                    "name": "Rue de Nivelles",
                                                                                    "way_points": [172, 183]},
                                                                                   {"distance": 15.3, "duration": 3.7,
                                                                                    "type": 0,
                                                                                    "instruction": "Turn left onto Place de l'Hôtel de Ville",
                                                                                    "name": "Place de l'Hôtel de Ville",
                                                                                    "way_points": [183, 184]},
                                                                                   {"distance": 0.0, "duration": 0.0,
                                                                                    "type": 10,
                                                                                    "instruction": "Arrive at Place de l'Hôtel de Ville, on the left",
                                                                                    "name": "-",
                                                                                    "way_points": [184, 184]}]}],
                                                                 "extras": {"roadaccessrestrictions": {
                                                                     "values": [[0, 24, 0], [24, 27, 16], [27, 184, 0]],
                                                                     "summary": [{"value": 0.0, "distance": 6555.8,
                                                                                  "amount": 98.89},
                                                                                 {"value": 16.0, "distance": 73.8,
                                                                                  "amount": 1.11}]}}, "warnings": [
                                                          {"code": 1,
                                                           "message": "There may be restrictions on some roads"}],
                                                                 "summary": {"distance": 6629.6, "duration": 607.5},
                                                                 "way_points": [0, 184]}, "geometry": {
        "coordinates": [[4.613003, 50.66821], [4.613007, 50.668189], [4.613059, 50.668107], [4.613083, 50.668087],
                        [4.61315, 50.668056], [4.613249, 50.668027], [4.613306, 50.668015], [4.613336, 50.668009],
                        [4.613559, 50.667975], [4.613722, 50.667951], [4.613778, 50.667945], [4.61385, 50.667945],
                        [4.613948, 50.667969], [4.614005, 50.667998], [4.614077, 50.668044], [4.614222, 50.668191],
                        [4.614259, 50.668232], [4.614527, 50.668511], [4.61459, 50.668578], [4.614619, 50.66861],
                        [4.614656, 50.66865], [4.614683, 50.66868], [4.615139, 50.669098], [4.615257, 50.669199],
                        [4.615481, 50.669438], [4.615616, 50.669581], [4.615999, 50.669893], [4.6161, 50.669972],
                        [4.616255, 50.670086], [4.616552, 50.670311], [4.616691, 50.670414], [4.616772, 50.670484],
                        [4.617098, 50.670727], [4.617873, 50.671299], [4.618497, 50.671749], [4.618557, 50.671793],
                        [4.618782, 50.671992], [4.61893, 50.672177], [4.619008, 50.672308], [4.619065, 50.67244],
                        [4.61911, 50.672579], [4.619135, 50.672679], [4.619203, 50.672955], [4.619214, 50.673004],
                        [4.619219, 50.673026], [4.619336, 50.673335], [4.619731, 50.673953], [4.61997, 50.674289],
                        [4.62017, 50.674519], [4.620358, 50.674691], [4.620691, 50.674914], [4.620972, 50.675052],
                        [4.62132, 50.675189], [4.622176, 50.675447], [4.62248, 50.675496], [4.622544, 50.675507],
                        [4.622588, 50.675488], [4.622674, 50.675463], [4.622768, 50.675451], [4.622838, 50.67545],
                        [4.622999, 50.67548], [4.623128, 50.675548], [4.623176, 50.675594], [4.623208, 50.675646],
                        [4.623329, 50.675712], [4.623471, 50.675753], [4.623588, 50.675769], [4.623692, 50.675789],
                        [4.623853, 50.675828], [4.623951, 50.675859], [4.624124, 50.675944], [4.624513, 50.676168],
                        [4.624743, 50.676362], [4.625422, 50.676843], [4.625871, 50.677037], [4.626302, 50.67718],
                        [4.626514, 50.677242], [4.627096, 50.677418], [4.627753, 50.677566], [4.628987, 50.677839],
                        [4.629515, 50.677958], [4.629707, 50.678008], [4.629878, 50.678075], [4.630007, 50.678151],
                        [4.630131, 50.678248], [4.630291, 50.678471], [4.630322, 50.678591], [4.6303, 50.67882],
                        [4.630151, 50.679037], [4.630018, 50.679139], [4.629831, 50.679241], [4.628106, 50.679915],
                        [4.627849, 50.68003], [4.627674, 50.680125], [4.627393, 50.680322], [4.62725, 50.680461],
                        [4.627097, 50.680659], [4.627, 50.680784], [4.626811, 50.680911], [4.625618, 50.683389],
                        [4.624302, 50.686082], [4.62304, 50.688651], [4.622141, 50.690424], [4.620919, 50.692631],
                        [4.619985, 50.69418], [4.619076, 50.695607], [4.617618, 50.697722], [4.617303, 50.698153],
                        [4.616724, 50.698932], [4.616114, 50.699717], [4.615211, 50.700842], [4.614, 50.702294],
                        [4.612709, 50.70375], [4.611784, 50.704727], [4.6111, 50.705389], [4.610447, 50.705975],
                        [4.609405, 50.706811], [4.608638, 50.707374], [4.607792, 50.707932], [4.607815, 50.708025],
                        [4.607508, 50.708227], [4.607225, 50.708465], [4.607099, 50.708638], [4.607026, 50.708888],
                        [4.60703, 50.709043], [4.607044, 50.70917], [4.607143, 50.709537], [4.607142, 50.709615],
                        [4.607079, 50.70976], [4.606932, 50.709908], [4.606846, 50.709968], [4.606393, 50.710261],
                        [4.606085, 50.710476], [4.605903, 50.710605], [4.605871, 50.710636], [4.605831, 50.710677],
                        [4.605783, 50.710832], [4.60583, 50.710959], [4.605861, 50.711004], [4.605994, 50.711034],
                        [4.606072, 50.711071], [4.606133, 50.711119], [4.606175, 50.711175], [4.606193, 50.711226],
                        [4.606194, 50.711278], [4.606178, 50.71133], [4.606235, 50.711397], [4.606363, 50.711488],
                        [4.606449, 50.711548], [4.606534, 50.711608], [4.607014, 50.711876], [4.607067, 50.711905],
                        [4.607137, 50.711945], [4.607313, 50.712047], [4.60737, 50.71214], [4.607553, 50.712247],
                        [4.607841, 50.712433], [4.607748, 50.712516], [4.607648, 50.712567], [4.607587, 50.712605],
                        [4.607595, 50.712878], [4.607599, 50.71292], [4.607588, 50.712999], [4.607579, 50.713062],
                        [4.607556, 50.713146], [4.607517, 50.713248], [4.60726, 50.713611], [4.607136, 50.71378],
                        [4.607008, 50.713892], [4.606929, 50.713961], [4.606883, 50.714001], [4.606852, 50.714033],
                        [4.606826, 50.714061], [4.607085, 50.71426], [4.607388, 50.714576], [4.607475, 50.714674],
                        [4.607711, 50.714965], [4.607806, 50.715102], [4.608036, 50.715434], [4.608113, 50.715569],
                        [4.608178, 50.71569], [4.608526, 50.71603], [4.608644, 50.71616], [4.608755, 50.716285],
                        [4.608574, 50.716361]], "type": "LineString"}}],
       "bbox": [4.605783, 50.667945, 4.630322, 50.716361],
       "metadata": {"attribution": "openrouteservice.org | OpenStreetMap contributors", "service": "routing",
                    "timestamp": 1638390811676,
                    "query": {"coordinates": [[4.6128839, 50.6682012], [4.60845, 50.7162425]], "profile": "driving-car",
                              "format": "json"}, "engine": {"version": "6.6.1", "build_date": "2021-07-05T10:57:48Z",
                                                            "graph_date": "2021-11-18T15:23:41Z"}}}
var = [{"place_id": 282683161, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
        "osm_type": "relation", "osm_id": 3417260,
        "boundingbox": ["50.6590954", "50.6894891", "4.5956956", "4.6483381"], "lat": "50.6682012", "lon": "4.6128839",
        "display_name": "Louvain-la-Neuve, Ottignies-Louvain-la-Neuve, Nivelles, Brabant wallon, Wallonie, 1348, Belgique",
        "class": "boundary", "type": "administrative", "importance": 0.7427124091390072,
        "icon": "https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},
       {"place_id": 57177702, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
        "osm_type": "node", "osm_id": 5041130444, "boundingbox": ["50.664712", "50.674712", "4.6110384", "4.6210384"],
        "lat": "50.669712", "lon": "4.6160384",
        "display_name": "Louvain-la-Neuve, Gallerie des Halles, Lauzelle, Louvain-la-Neuve, Ottignies-Louvain-la-Neuve, Nivelles, Brabant wallon, Wallonie, 1348, Belgique",
        "class": "railway", "type": "station", "importance": 0.5874189406975714,
        "icon": "https://nominatim.openstreetmap.org/ui/mapicons//transport_train_station2.p.20.png"},
       {"place_id": 100058, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
        "osm_type": "node", "osm_id": 144959, "boundingbox": ["50.6810079", "50.6811079", "4.6264192", "4.6265192"],
        "lat": "50.6810579", "lon": "4.6264692",
        "display_name": "Louvain-la-Neuve, E411, La Baraque, Louvain-la-Neuve, Ottignies-Louvain-la-Neuve, Nivelles, Brabant wallon, Wallonie, 1348, Belgique",
        "class": "highway", "type": "motorway_junction", "importance": 0.30100000000000005},
       {"place_id": 61702184, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
        "osm_type": "node", "osm_id": 5604104640, "boundingbox": ["50.6705917", "50.6706917", "4.6171966", "4.6172966"],
        "lat": "50.6706417", "lon": "4.6172466",
        "display_name": "Louvain-la-Neuve, Boulevard de Wallonie-Sud, Lauzelle, Louvain-la-Neuve, Ottignies-Louvain-la-Neuve, Nivelles, Brabant wallon, Wallonie, 1348, Belgique",
        "class": "railway", "type": "stop", "importance": 0.30100000000000005},
       {"place_id": 61736525, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
        "osm_type": "node", "osm_id": 5604104642, "boundingbox": ["50.670494", "50.670594", "4.6173957", "4.6174957"],
        "lat": "50.670544", "lon": "4.6174457",
        "display_name": "Louvain-la-Neuve, Voie des Hennuyers, Lauzelle, Louvain-la-Neuve, Ottignies-Louvain-la-Neuve, Nivelles, Brabant wallon, Wallonie, 1348, Belgique",
        "class": "railway", "type": "stop", "importance": 0.30100000000000005},
       {"place_id": 111340848, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
        "osm_type": "way", "osm_id": 38652974, "boundingbox": ["50.6674207", "50.6680871", "4.6128961", "4.6138391"],
        "lat": "50.667778850000005", "lon": "4.613385154195076",
        "display_name": "Louvain-La-Neuve, Gare d'Autobus, Boulevard du Sud, Biéreau, Louvain-la-Neuve, Ottignies-Louvain-la-Neuve, Nivelles, Brabant wallon, Wallonie, 1348, Belgique",
        "class": "amenity", "type": "bus_station", "importance": 0.30100000000000005,
        "icon": "https://nominatim.openstreetmap.org/ui/mapicons//transport_bus_station.p.20.png"},
       {"place_id": 229729, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
        "osm_type": "node", "osm_id": 60286173, "boundingbox": ["50.6595896", "50.6596896", "4.608404", "4.608504"],
        "lat": "50.6596396", "lon": "4.608454",
        "display_name": "N223;Louvain-la-Neuve;Biéreau;Bruyère, N238, Ottignies, Ottignies-Louvain-la-Neuve, Nivelles, Brabant wallon, Wallonie, 1340, Belgique",
        "class": "highway", "type": "motorway_junction", "importance": 0.30100000000000005},
       {"place_id": 721816, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
        "osm_type": "node", "osm_id": 267816832, "boundingbox": ["50.6782198", "50.6783198", "4.6281294", "4.6282294"],
        "lat": "50.6782698", "lon": "4.6281794",
        "display_name": "Louvain-la-Neuve, E411, Val Villers, Chaumont-Gistoux, Nivelles, Brabant wallon, Wallonie, 1325, Belgique",
        "class": "highway", "type": "motorway_junction", "importance": 0.30100000000000005}]
