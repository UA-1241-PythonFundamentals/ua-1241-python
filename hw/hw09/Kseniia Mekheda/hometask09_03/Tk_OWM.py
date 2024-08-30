import tkinter as tk
from tkinter import font
import OWM

HEIGHT = 350
WIDTH = 600


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

def get_weather():
    place = entry_field.get()
    observation = OWM.mgr.weather_at_place(place)
    w = observation.weather
    detailed_status_label = tk.Label(lower_frame, text=f"Status: {w.detailed_status}")
    detailed_status_label.pack()
    wind_label = tk.Label(lower_frame, text=f"Wind: {w.wind()}")
    wind_label.pack()
    humidity_label = tk.Label(lower_frame, text=f"Humidity: {w.humidity}")
    humidity_label.pack()
    temperature_label = tk.Label(lower_frame, text=f"Temperature: {w.temperature('celsius')}")
    temperature_label.pack()
    rain_label = tk.Label(lower_frame, text=f"Rain: {w.rain}")
    rain_label.pack()
    heat_index_label = tk.Label(lower_frame, text=f"Heat Index: {w.heat_index}")
    heat_index_label.pack()
    clouds_label = tk.Label(lower_frame, text=f"Clouds: {w.clouds}")
    clouds_label.pack() 

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.95, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

