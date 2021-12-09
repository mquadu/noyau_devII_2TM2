from request.request import Request
from bot.bot import Bot
# from app import ChatBot


if __name__ == "__main__":
    rep = input("Entrez une commmande \t")  # La classe request doit récupérer le request de l'utilisateur et son
    # pseudo
    # ChatBot.run()

    # rep = ChatBot.send_info("")

    # print(rep)
    command_list = ["/help", "/weather", "/itinerary", "/resto", "/cine", "/news", "/opinion"]
    message = Request(rep)
    Bot(message, command_list)

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
