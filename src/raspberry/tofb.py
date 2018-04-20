#import Libraries
import RPi.GPIO as GPIO
import time
import pyrebase
import requests
import datetime
import socket
import serial
import petcense



def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def startService():
    import os
    os.system("sudo service motion start")

def stopService():
    import os
    os.system("sudo service motion stop")
    
def sendNotification(text1, text2):
    text1 = text1.replace(" ", "%20")
    text2 = text2.replace(" ", "%20")
    requests.get("http://tongue-lash-adverbs.000webhostapp.com/Notification.php?title={}&msg={}".format(text1, text2))
    time.sleep(2)

def stream_handler(message):
 #    print(message["event"]) # put
    print(message["path"]) # /Alarma
    print(message["data"]) # {'Estado': 'false', 'odigo': '1234'}

def config_firebase():
    #Firebase Configuration
    config = {
      "apiKey": "AIzaSyDVLsHqEpgpI679wT2MS-tcFFG04axvgAA",
      "authDomain": "petcense.firebaseapp.com",
      "databaseURL": "https://petcense.firebaseio.com",
      "storageBucket": "petcense.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)
    #Firebase Database Intialization
    db = firebase.database()
    print("{}".format(get_ip_address()))
    my_stream = db.child("").stream(stream_handler)           

def Set_hist_Acceso():
    tempHist=db.child("acceso/HistorialAcc").get()
    db.child("acceso").update({"HistorialAcc": tempHist+"&"+var_hora()}

def Set_hist_Alimentacion
    tempHist=db.child("Alimentacion/HistorialAl").get()
    db.child("Alimentacion").update({"HistorialAl": tempHist+"&"+var_hora()})

                              
 
        
except KeyboardInterrupt:
    my_stream.close()
    ser.close()
    
    print("Everything Closed!")



