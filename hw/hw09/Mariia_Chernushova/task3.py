import tkinter as tk
from tkinter import font
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather():
    city = entry_field.get()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    label["text"] = f"""In the city {city} now {w.detailed_status}\n
    Average wind speed: {w.wind()['speed']} m/s\n
    Humidity: {w.humidity} %\n
    Air temperature: {w.temperature('celsius')['temp']} degrees\n
    The air will warm up to a maximum of {w.temperature('celsius')['temp_max']} degrees\n
    The minimum air temperature will be {w.temperature('celsius')['temp_min']} degrees\n
    Rain: {w.rain}\n
    Clouds: {w.clouds}"""
     
HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 18))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="grey", fg="white", 
                   font=('Courier', 16), 
                   command= get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, text=" ",font=('Courier', 12), anchor='n')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()