from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_w_to_str(w):
    return f'{w.detailed_status} \n {w.wind()} \n {w.humidity} \n {w.temperature('celsius')}'

# Search for current weather in London (Great Britain) and get details

def get_weather_data(city):    
    observation = mgr.weather_at_place(city) 
    w = observation.weather
    # print(w.detailed_status)       
    # print(w.wind())                  
    # print(w.humidity)                
    # print(w.temperature('celsius'))  
    # print(w.rain),                    
    # print(w.heat_index)            
    # print(w.clouds)                  
    return get_w_to_str(w)





