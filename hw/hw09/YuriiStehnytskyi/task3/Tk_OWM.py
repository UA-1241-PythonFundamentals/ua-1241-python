from pyowm import OWM
import tkinter as tk
from tkinter import font

# API Key and Weather Manager setup
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# Function to fetch and display weather information
def get_weather():
    city = entry_field.get()  # Get the city from the entry widget
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        
        # Build the weather result string
        weather_info = (
            f"Weather in {city}:\n"
            f"Status: {w.detailed_status}\n"
            f"Wind Speed: {w.wind()['speed']} m/s\n"
            f"Humidity: {w.humidity}%\n"
            f"Temperature: {w.temperature('celsius')['temp']}°C\n"
            f"Cloud coverage: {w.clouds}%\n"
        )
    except Exception as e:
        weather_info = "City not found or error fetching weather."
    
    # Display weather information in the label
    label['text'] = weather_info

# GUI setup
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
                   command=get_weather)  # Calls the get_weather function
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), anchor='nw', justify='left', bd=4)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
