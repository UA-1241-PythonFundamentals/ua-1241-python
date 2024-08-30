import tkinter as tk
from tkinter import font
import OWM

HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()
w_list = ""


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

def get_weather():
    w = OWM.mgr.weather_at_place(entry_field.get()).weather
    w_list = str(w.detailed_status) + '\n'         # 'clouds'
    w_list += str(w.wind()) + '\n'                 # {'speed': 4.6, 'deg': 330}
    w_list += str(w.humidity) + '\n'                # 87
    w_list += str(w.temperature('celsius')) + '\n'  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    w_list += str(w.clouds) + '\n'
    label.config(text = w_list)   

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="black", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, 
                 font=('Courier', 14),
                 text= str(w_list))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

