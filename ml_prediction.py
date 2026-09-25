{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pandas as pd\
import matplotlib.pyplot as plt\
from sklearn.linear_model import LinearRegression\
import datetime\
import requests\
import time\
\
TOKEN = "Qu4P2356MOczKucLW1Z3Ijl1YnIqaPw7"\
\
URL = f"https://blynk.cloud/external/api/get?token=\{TOKEN\}&V1"\
\
history = []\
\
while True:\
\
    try:\
        current = int(requests.get(URL).text)\
    except:\
        current = 0\
\
    hour = datetime.datetime.now().hour\
\
    history.append([hour,current])\
\
    df = pd.DataFrame(history,columns=["hour","count"])\
\
    if len(df) > 3:\
\
        X = df[["hour"]]\
        y = df["count"]\
\
        model = LinearRegression()\
        model.fit(X,y)\
\
        hours = list(range(0,24))\
        pred = model.predict(pd.DataFrame(hours,columns=["hour"]))\
\
        plt.figure()\
\
        plt.scatter(df["hour"],df["count"],label="Actual")\
        plt.plot(hours,pred,label="Prediction")\
\
        plt.xlabel("Hour")\
        plt.ylabel("Cars Parked")\
        plt.title("Parking Occupancy Prediction")\
\
        plt.legend()\
        plt.grid()\
\
        plt.savefig("graph.png")\
        plt.close()\
\
        print("Graph updated")\
\
    time.sleep(20)}