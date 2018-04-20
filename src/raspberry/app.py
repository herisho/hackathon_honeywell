import petcense
import time
import tofb

db = tofb.config_firebase()

puerta = petcense.setupSerial('/dev/ttyUSB0')
#comida = petcense.setupSerial('/dev/ttyACM')

while True:

    petcense.acceso(puerta,db)
#   petcense.alimentacion(comida)
    time.sleep(10)
    
