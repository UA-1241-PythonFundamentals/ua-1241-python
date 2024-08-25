import tkinter as tk
from tkinter import font
from pyowm import OWM

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
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

def get_weather(city):
    try:
        # Отримуємо погоду для введеного міста
        observation = mgr.weather_at_place(city)
        w = observation.weather
        
        # Формуємо інформацію для відображення
        temperature = w.temperature('celsius')
        weather_info = f"City: {city}\n"
        weather_info += f"Status: {w.detailed_status}\n"
        weather_info += f"Temperature: {temperature['temp']}°C\n"
        weather_info += f"Humidity: {w.humidity}%\n"
        weather_info += f"Wind Speed: {w.wind()['speed']} m/s\n"
        
        # Оновлюємо текст у віджеті label
        label.config(text=weather_info)
    except Exception as e:
        # Відображаємо повідомлення про помилку, якщо місто не знайдено
        label.config(text="City not found. Please try again.")


root.mainloop()

