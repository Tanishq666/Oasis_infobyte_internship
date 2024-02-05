from tkinter import *
import requests
import json
import datetime

api_key = "f09c11722cdcc7063709441fb23ab1c7"

window = Tk()
window.title("Weather Forecast")
window.config(width=450, height=700, bg="white")

dt = datetime.datetime.now()
date = Label(text=dt.strftime('%A--'), bg="white", font=("bold",14))
date.place(x=5,y=100)
month = Label(text=dt.strftime('%m %B'), bg="white", font=("bold", 14))
month.place(x=100, y=100)

hour = Label(text=dt.strftime('%I : %M %p'), bg="white", font=("bold", 14))
hour.place(x=10, y=140)

city_name = StringVar()
city_entry = Entry(textvariable=city_name, width=45)
city_entry.place(x=0,y=10)


def city_name():
    api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city_entry.get()+"&units=metric&appid="+api_key)
    api = json.loads(api_request.content)

    y = api['main']
    current_temprature = y['temp']
    humidity = y['humidity']
    tempmin = y['temp_min']
    tempmax = y['temp_max']

    x = api['coord']
    longitude = x['lon']
    latitude = x['lat']

    z = api['sys']
    country = z['country']
    city =api['name']

    label_temp.config(text=current_temprature)
    label_lon.config(text=longitude)
    label_lat.config(text=latitude)
    label_country.config(text=country)
    label_city.config(text=city)
    max_temp.config(text=tempmax)
    min_temp.config(text=tempmin)
    humidity_label.config(text=humidity)


city_name_button = Button(text="Search", command=city_name)
city_name_button.place(x=280,y=10)

label_city = Label(text="...", width=0, bg="white", font=("bold", 15))
label_city.place(x=10, y=40)

label_country = Label(text="...", width=0, bg="white", font=("bold", 15))
label_country.place(x=125, y=40)

label_lon = Label( text="...", width=0,  bg='white', font=("Helvetica", 15))
label_lon.place(x=10, y=70)
label_lat = Label( text="...", width=0, bg='white', font=("Helvetica", 15))
label_lat.place(x=95, y=70)

humidity = Label(text="Humidity: ", width=0, bg="white",font=("bold",15))
humidity.place(x=3,y=400)

humidity_label = Label(text="...", width=0,bg='white',font=("bold",15))
humidity_label.place(x=107, y=400)

label_temp = Label(text="...", width=0, bg='white',
                   font=("Helvetica", 110), fg='black')
label_temp.place(x=18, y=220)

maxi = Label(text="Max. Temp.: ", width=0,bg='white', font=("bold", 15))
maxi.place(x=3, y=430)

max_temp = Label(text="...", width=0, bg='white', font=("bold", 15))
max_temp.place(x=128, y=430)

mini = Label(text="Min. Temp.: ", width=0,bg='white', font=("bold", 15))
mini.place(x=3, y=460)

min_temp = Label(text="...", width=0,bg='white', font=("bold", 15))
min_temp.place(x=128, y=460)

note = Label(text="All temperatures in degree celsius", bg='white', font=("italic", 10))
note.place(x=95, y=495)


window.mainloop()
