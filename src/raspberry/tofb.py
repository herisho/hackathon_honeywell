#import Libraries
import RPi.GPIO as GPIO
import time
import pyrebase
import smbus
import Adafruit_DHT
import requests
import datetime
import socket
import serial



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

try:
    while(True):
        

        if (ser.inWaiting() > 0):
            rec = ser.read(ser.inWaiting())
            print(rec)
            data=rec.decode('utf-8')

            
            tempHist=db.child("Alimentacion/Historial").get()
            db.child("Alimentacion").update({"Historial": tempHist+";"+var_hora()})

            tempHist=db.child("acceso/Historial").get()
            db.child("acceso").update({"Historial": tempHist+";"+var_hora()+","+estado}

            
            
            if (b'sensor' in rec):
                sendNotification("Detección de sensores!", "Precione para iniciar")

            if (rec==b'L2\r\n'):
                db.child("Luces").update({"luz2": '"true"'})
        
except KeyboardInterrupt:
    my_stream.close()
    ser.close()
    
    print("Everything Closed!")



