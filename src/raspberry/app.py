import petcense
import time


puerta = petcense.setupSerial('/dev/tty.usbserial0')
comida = petcense.setupSerial('/dev/tty.usbserial1')

while True:

    petcense.acceso(puerta)
    petcense.alimentacion(comida)
    time.sleep(10)
    