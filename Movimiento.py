import os
from gpiozero import MotionSensor
import telebot
class Motion():
	def __init__(self,bot):
		pir=MotionSensor(4)
	def 
# Si se detecta movimiento se imprime en consola, se manda mensaje a telegram y se enciende el led
while True:
    pir.wait_for_motion()
    print("Se detectó intruso")
    bot.send_message("1320071778","Se detectó intruso")
    led.on()
    pir.wait_for_no_motion()
    led.off()
