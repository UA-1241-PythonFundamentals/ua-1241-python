import tkinter as tk
from tkinter import font
from pyowm import OWM



API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather():
    sity = entry_field.get()
    try:
        observation = mgr.weather_at_place(sity)
        w = observation.weather

        detals_weather  = (
            f"Sity : {sity}:\n"
            f"Status: {w.detailed_status}\n"
            f"Wind : {w.wind()['speed']} m/s\n"
            f"Humidity: {w.humidity}%\n"
            f"Temperature: {w.temperature('celsius')['temp']}°C\n"
            f"Rain: {w.rain}\n"
            f"Heat index: {w.heat_index}\n"
            
            
            f"Cloud : {w.clouds}%\n"
        )
        label['text'] = detals_weather
    except:
        label['text'] = 'Error input real sity'
    

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
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()