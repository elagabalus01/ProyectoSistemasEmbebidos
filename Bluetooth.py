from bluedot import BlueDot
from signal import pause
from gpiozero import PWMLED

class Bluetooth():
    def __init__(self):
        encendido=False
        led_habitacion = PWMLED(13)
        bd = BlueDot()
        bd.when_pressed = self.prenderApagarLed

    def prenderApagarLed():
        '''Enciende un led'''
        if(not self.encendido):
            led_habitacion.value = 1
            self.encendido=True
        else:
            # SI ya está encendido se apaga
            led_habitacion.value = 0
            self.encendido=False

ctlBluetooth=Bluetooth()
