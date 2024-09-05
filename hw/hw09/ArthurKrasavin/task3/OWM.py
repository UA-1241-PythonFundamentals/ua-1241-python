def get_weather(city):
    from pyowm import OWM

    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

# Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(city)
    w = observation.weather

    w.detailed_status         # 'clouds'
    w.wind()                  # {'speed': 4.6, 'deg': 330}
    w.humidity                # 87
    w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    w.rain                    # {}
    w.heat_index              # None
    w.clouds                  # 75

    return f"Weather: {w.detailed_status}\nWind: {w.wind()['speed']} m/s\nHumidity: {w.humidity}%\nTemperature: {w.temperature('celsius')['temp']}°C\nRain: {w.rain}\nHeat Index: {w.heat_index}\nClouds: {w.clouds}"