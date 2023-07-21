#Importing required libraries
import json
from urllib.request import urlopen
import requests
#from sklearn import linear_model
#from sklearn.metrics import r2_score
import numpy as np
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
from selenium.webdriver import Chrome
#from selenium.webdriver.chrome.service import Service
#from sklearn.model_selection import train_test_split
import math
import pandas
from ipywidgets import interact
import ipywidgets as widgets
from IPython.display import *
out = widgets.Output()
def plot2(b=None):
    print('Ready')
    a=[]
    a0=[]
    #count
    print('Wait till result is shown!')
    a=[]
    a0=[]
        #country = input("1 for Jakarta, 2 for Delhi")
    if country == 1:
        page = requests.get('https://weather.com/en-IN/weather/hourbyhour/l/cc76c08b470b5ddd6e64efd9ce8f256542cfed4ba52f6c00a30a74da519cd070')
    else:
        page = requests.get('https://weather.com/en-IN/weather/hourbyhour/l/cd5287a9b7c6082e70de21891369ada61322a7aa1fc24cca26803dcbd75c78d9')
    soup = BeautifulSoup(page.content, 'html.parser')
    blog=soup.findAll('span',attrs={"class":"Wind--windWrapper--3Ly7c undefined"})
    if True:
        for title in blog:
            k=title.text
            k1=k.split(' ')[1]
            #print(k1)
            a.append(k.split(' ')[0])
            if(k1[1]!='1' and k1[1]!='2' and k1[1]!='3' and k1[1]!='4' and k1[1]!='5' and k1[1]!='6'and k1[1]!='7' and k1[1]!='8'and k1[1]!='9' and k1[1]!='0'):
                a0.append(float(k1[0]))
                print(a0)
            else:
                a0.append(float(k1[0])*10+float(k1[1]))
        x2=a0
        y2=[]
        #df = pandas.read_csv("AQI.csv")
        x0 = json.load(urlopen("https://ipinfo.io/"))['loc'].split(',')
        x1=float(x0[0])
        xmax=x1
        xmin=x1
        y=float(x0[1])
        ymax=y
        ymin=y
        #X = df[['Avg1', 'Avg2','Avg3','Avg5']].values
        #print(X)
        #y1 = df['AQI']
        #print(y)
        #regr = linear_model.LinearRegression()
        #regr.fit(X,y1)
        #x=regr.predict([[9/5*avg1+32,9/5*avg2+32,avg3,avg5*0.02953]])

        #Printing predicted AQI

        #Converting past wind to vectors to track pollutants
        for i in a:
            if i=='N':
                y2.append(0)
            elif i=='NW':
                y2.append(-45)
            elif i=='WNW':
                y2.append(-67.5)
            elif i=='NNW':
                y2.append(-22.5)
            elif i=='NE':
                y2.append(45)
            elif i=='ENE':
                y2.append(67.5)
            elif i=='NNE':
                y2.append(22.5)
            elif i=='S':
                y2.append(180)
            elif i=='SW':
                y2.append(225)
            elif i=='WSW':
                y2.append(237.5)
            elif i=='SSW':
                y2.append(202.5)
            elif i=='SE':
                y2.append(135)
            elif i=='ESE':
                y2.append(112.5)
            elif i=='SSE':
                y2.append(157.5)
            elif i=='W':
                y2.append(-90)
            elif i=="E":
                y2.append(90)
        #Converting
        for i in range(len(y2)):
            y2[i]=y2[i]*math.pi/180
        #print(x1)
        #print(y)
        #number = input("Enter number <10")
        number = int(freq_slider)
        for i in range(int(number)):
            x1=x1-(x2[i]*math.cos(y2[i]))*1/54.6
            xmax=xmax-(x2[i]*math.cos(y2[i]+22.5*math.pi/180))*1/54.6
            xmin=xmin-(x2[i]*math.cos(y2[i]-22.5*math.pi/180))*1/54.6
            y=y-(x2[i]*math.sin(y2[i]))*1/54.6
            ymax=ymax-(x2[i]*math.sin(y2[i]+22.5*math.pi/180))*1/54.6
            ymin=ymin-(x2[i]*math.sin(y2[i]-22.5*math.pi/180))*1/54.6

        #Finding distance from pollution center
        A1=[]
        A2=A1
        A2.sort()
        X_1=x1
        Y_1=y
        #Finding current AQI and comparing to forecasted API
        blog=soup.findAll('text',attrs={"data-testid":"DonutChartValue"})
        i=0
        for title in blog:
            k=title.text
            if(i>=1):
                break
            i=i+1
        AQI=float(k)
        x=AQI
        print('AQI:')
        if x<50:
            print('Level 1')
        elif x<101:
            print('Level 2')
        elif x<150:
            print("Level 3")
        elif x<200:
            print("Level 4")
        elif x<300:
            print("Level 5")
        else:
            print("V Bad")
        #print(x[0])

        #Printing possible sources from our calculated coordinates and deciding penalty by comparing AQI
        #
        #print("%.4f"%x1)
        #print("%.4f"%y)
        # Latitude & Longitude input
        coordinates = str(x1)+","+str(y)
        print("Pollutants coming in "+str(color_buttons.value)+" "+str(freq_slider.value))
        print("https://www.google.com/maps/search/"+str(coordinates))
        #location = geolocator.reverse(coordinates)
        #address = location.raw['address']
        #print(address)
        #print('https://pin-code.org.in/companies/viewall/'+str(address['postcode']))
from ipywidgets import Dropdown
color_buttons = genre = st.radio(
    "What\'s your city",
    ('Jakarta', 'Delhi'))
freq_slider = st.radio(
    "What",
    ('1', '2','3','4','5','6','7','8','9'))
if st.button("Compute"):
    plot2()
#_slider = st.FloatSlider(value=2,min=1,max=10,step=1,description='Frequency:',readout_format='.0f',)
#color_buttons.observe(plot2)
#freq_slider.observe(plot2)
from ipywidgets import HBox, VBox
#VBox([container, g])
#@button.on_click
#def plot(b):
    #plot2()
#print("What is your location? How many hours back do you want to track the wind and pollution?")
#container = HBox([color_buttons, freq_slider, button])
#container
