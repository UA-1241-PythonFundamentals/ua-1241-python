import tkinter as tk
from tkinter import font
from OWM import *


def get_weather():
    observation = mgr.weather_at_place(entry_field.get())
    w = observation.weather
    label = tk.Label(lower_frame, font=('Courier', 12),
                     text = f"Status: {w.detailed_status}\n\n"
                            f"Wind: {w.wind()}\n\n"
                            f"Humidity: {w.humidity}\n\n"
                            f"Temperature('celsius'): Temp: {w.temperature('celsius')['temp']}\n"
                            f"                        Max temp.: {w.temperature('celsius')['temp_max']}\n"
                            f"                        Feels like: {w.temperature('celsius')['feels_like']}\n"
                            f"                        Kf.temp.: {w.temperature('celsius')['temp_kf']}\n"
                            f"Rain: {w.rain}\n\n"
                            f"Heat index: {w.heat_index}\n\n"
                            f"Clouds: {w.clouds}", justify="center")
    label.place(relx=0, rely=0, relwidth=1, relheight=1)

HEIGHT = 350
WIDTH = 450

root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

root.mainloop()
