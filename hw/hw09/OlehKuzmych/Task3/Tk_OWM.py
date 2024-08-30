import tkinter as tk
from tkinter import font
import OWM

def update_weather():
    weather = OWM.get_weather(entry_field.get())

    weather_label.config(text=f"City: {weather['city']}")
    detailed_status_label.config(text=f"Status: {weather['weather']['detailed_status']}")
    wind_label.config(text=f"Wind: {weather['weather']['wind']}")
    humidity_label.config(text=f"Humidity: {weather['weather']['humidity']}")
    temperature_label.config(text=f"Temperature: {weather['weather']['temperature']['temp']}")
    rain_label.config(text=f"Rain: {weather['weather']['rain']}")
    heat_index_label.config(text=f"Heat Index: {weather['weather']['heat_index']}")
    clouds_label.config(text=f"Clouds: {weather['weather']['clouds']}")


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
                   command=update_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

weather_label = tk.Label(lower_frame, text="City: ")
weather_label.pack()
detailed_status_label = tk.Label(lower_frame, text="Status: ")
detailed_status_label.pack()
wind_label = tk.Label(lower_frame, text="Wind: ")
wind_label.pack()
humidity_label = tk.Label(lower_frame, text="Humidity: ")
humidity_label.pack()
temperature_label = tk.Label(lower_frame, text="Temperature: ")
temperature_label.pack()
rain_label = tk.Label(lower_frame, text="Rain: ")
rain_label.pack()
heat_index_label = tk.Label(lower_frame, text="Heat Index: ")
heat_index_label.pack()
clouds_label = tk.Label(lower_frame, text="Clouds: ")
clouds_label.pack()

root.mainloop()
