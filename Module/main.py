

if __name__ == "__main__":
    rep = input("Entrez une commmande \t")
    rep_split = rep.split(" ")  # Cas ou il entre le weather avec paramètre

    if rep_split[0] == "/help":

        Commande().help()

    elif rep_split[0] == "/weather":

        if len(rep_split) == 2:
            commande = Commande(rep_split[1]).weather
            print(commande)
        else:
            commande = Commande().weather
            print(commande)
    else:
        print("Erreur dans la weather!")


"""
Exemple de retour json
{'request': {'type': 'City', 'query': 'Louvain-La-Neuve, Belgium', 'language': 'en', 'unit': 'm'}, 
'location': {'name': 'Louvain-La-Neuve', 'country': 'Belgium', 'region': '', 'lat': '50.683', 'lon': '4.617', 
'timezone_id': 'Europe/Brussels', 'localtime': '2021-11-10 20:36', 'localtime_epoch': 1636576560, 'utc_offset': '1.0'}, 
'current': {'observation_time': '07:36 PM', 'temperature': 7, 'weather_code': 113, 
'weather_icons': ['https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 
'weather_descriptions': ['Clear'], 'wind_speed': 0, 'wind_degree': 209, 'wind_dir': 'SSW', 'pressure': 1024,'precip': 0,
'humidity': 81, 'cloudcover': 0, 'feelslike': 6, 'uv_index': 1, 'visibility': 9, 'is_day': 'no'}}
"""
