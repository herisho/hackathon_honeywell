#usr/bin/python
#encode *utf-8*
#Hackathon honeywell

import serial
import time
from datetime import datetime


def setupSerial(portName):
    return serial.Serial(port= portName, baudrate= 9600)

def leer_serial(serial):
    return seral.readline()

def escribir_serial(serial, data):
    serial.write(data)


def checkHour(date):
    fed_morining_start = datetime(datetime.now().year, datetime.now().month, 8)
    fed_morining_finish = datetime(datetime.now().year, datetime.now().month, 9)
    fed_afternoon_start = datetime(datetime.now().year, datetime.now().month, 17)
    fed_afternoon_finish = datetime(datetime.now().year, datetime.now().month, 18)

    if (fed_morining_start < date < fed_morining_finish) or (fed_afternoon_start < date < fed_afternoon_finish):
        return True
    else:
        return False


def Acceso():
    data = leer_serial(puerta)
    if data == b'a/n/r':
        
    
def alimentacion():
    data = leer_serial(comida)
    if data == b'c/n/r':
        if checkHour():
            escribir_serial(comida, b'y/n/r')
        else:
            escribir_serial(comida, b'n/n/r')
            