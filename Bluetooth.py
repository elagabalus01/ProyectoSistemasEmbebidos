# Importación de bibliotecas
from bluedot import BlueDot
from signal import pause
from gpiozero import PWMLED

# Clase Bluetooth, para controlar el dispositivo vía Bluetooth
class Bluetooth():

    # Función para inicializar clase
    def __init__(self,led):
        self.led_habitacion = led
        self.bd = BlueDot()
        self.bd.when_pressed = self.prenderApagarLed

    # Función para prender y apagar led por Bluetooth
    def prenderApagarLed(self):
        if(not self.led_habitacion.value == 1):
            self.led_habitacion.value = 1
        else:
            self.led_habitacion.value = 0

# Función main de la clase Bluetooth
if __name__=="__main__":
	ctlBluetooth=Bluetooth()
	pause()
