#usr/bin/python
#encode *utf-8*
#Hackathon honeywell

import serial
import algo
from datetime import datetime

global fed
fed = False

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
        fed = False 
        return False


def acceso(ser):
    data = leer_serial(ser)
    if data == b'a/n/r':
        
    
def alimentacion(ser):
    data = leer_serial(ser)
    if data == b'c/n/r':
        if checkHour():
            if not fed:
                escribir_serial(ser, b'y/n/r')
                print(var_hora())
                fed = True
        else:
            escribir_serial(ser, b'n/n/r')
            cont += 1
            if cont > 10:
                algo.send_notificacion('Alimentacion', 'Tu mascota quiere comer')
            
def var_hora():
    return datetime.now()

