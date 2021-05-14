# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:32:15 2021

@author: apoor
"""

import requests, json
import tkinter as tk
import time
import datetime
from datetime import date


def showWeather():
    today = date.today()
    d2 = today.strftime("%B %d,\n %Y")
    now = datetime.datetime.now()

    a=now.strftime("%I:%M%p")



    api_key = "874bf9b7e750c4e2304510b98f184d01"
    
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    

    city_name = 'thrissur'
    

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    

    response = requests.get(complete_url) 
    
    
    x = response.json()

    root=tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    geometry = str(screen_width) + "x" + str(screen_height)
    root.geometry(geometry)
    root.configure(background='black')


    Upper_right = tk.Label(root,text =  a + "\n" + str(d2))
    Upper_right.config(font =("Verdana", 20))
    Upper_right.config(background='black')
    Upper_right.config(foreground='white')

    Upper_right.place(relx = 1.0, 
                    rely = 0.0,
                    anchor ='ne')
    
    

    if x["cod"] != "404": 
    
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
    
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
    
        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 
    
        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 
    
        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 
    
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = z[0]["description"] 
    
        # print following values 
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description))
        Lower_left= tk.Label(root, text="Temperature = " + str(current_temperature)+"F" + "\natmospheric pressure= " + str(current_pressure)+"hpa" + "\nhumidity= " + str(current_humidiy)+"%" +"\ndescription= " + str(weather_description))
        Lower_left.config(font =("Verdana", 20))
        Lower_left.config(background='black')
        Lower_left.config(foreground='white')
        Lower_left.place(anchor ='nw')
        if( str(weather_description)== 'mist'):
            print("mist")
    
    else: 
        print(" City Not Found ")


    
    def NewsFromBBC():
        
        # BBC news api
        # following query parameters are used
        # source, sortBy and apiKey
        query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "943d64185d5e42998cf5448be43a8d66"
        }
        main_url = " https://newsapi.org/v1/articles"
    
        # fetching data in json format
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
    
        # getting all articles in a string article
        article = open_bbc_page["articles"]
    
        # empty list which will 
        # contain all trending news
        results = []
        
        for ar in article:
            results.append(ar["title"])
            
        for i in range(5):
            
            # printing all trending news
            i=i+1
            a=results[i]
            
        
        
            print(a)
        
            
            Upper_right = tk.Label(root,text = a )
            Upper_right.config(font =("Verdana", 20))
            Upper_right.config(background='black')
            Upper_right.config(foreground='white')

            Upper_right.place(relx = 0.5, 
                            rely = 0.5,
                            anchor ='center')
        
        
    NewsFromBBC()

    root.mainloop()