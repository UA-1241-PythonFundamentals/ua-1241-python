from pyowm import OWM
import tkinter as tk
from tkinter import font

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather():
    location = entry_field.get()
    try:
        observation = mgr.weather_at_place(location)
        w = observation.weather

        weather_details = (
            f"Weather in {location}:\n"
            f"Status: {w.detailed_status}\n"
            f"Temperature: {w.temperature('celsius')['temp']}°C\n"
            f"Max Temp: {w.temperature('celsius')['temp_max']}°C\n"
            f"Min Temp: {w.temperature('celsius')['temp_min']}°C\n"
            f"Wind Speed: {w.wind()['speed']} m/s\n"
            f"Humidity: {w.humidity}%\n"
            f"Cloud Coverage: {w.clouds}%\n"
        )
        label['text'] = weather_details
    except Exception as e:
        label['text'] = "Could not retrieve weather data. Please check the location name."

HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
