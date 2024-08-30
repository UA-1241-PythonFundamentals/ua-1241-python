import tkinter as tk
from tkinter import font
from pyowm import OWM

# Налаштування інтерфейсу
HEIGHT = 350
WIDTH = 450

# Ваш API ключ
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# Функція для отримання погоди
def get_weather():
    city = entry_field.get()
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        temperature = w.temperature('celsius')['temp']
        weather_description = w.detailed_status
        wind = w.wind()['speed']
        humidity = w.humidity

        final_str = f"City: {city}\nTemperature: {temperature}°C\nWeather: {weather_description}\nWind Speed: {wind} m/s\nHumidity: {humidity}%"
    except:
        final_str = "There was a problem retrieving the information."

    label['text'] = final_str

# Налаштування графічного інтерфейсу
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
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), anchor='nw', justify='left', bd=4)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
