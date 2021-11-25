'''
Programa controlador de hardware de Raspberry y servidor web
'''

# Importación de bibliotecas
from Bluetooth import Bluetooth
from time import sleep
from threading import Thread
from signal import pause
from Telegram import getServiceBot
from gpiozero import LED, MotionSensor
from TemperaturaHumedad import TemperaturaHumedad
from Movimiento import Movimiento
from Lightshow import LightShow
from AsistenteVirtual import AsistenteVirtual
from GoogleAssistant import GoogleAssistant
from Bomba import Bomba
from LedHab import LedHab
from piHomeDashboard import PiHome
from piHomeDashboard.PiHome import app
from flask import Flask, url_for

# Definición de funciones para controlar hilos
def bluetooth_connection(led):
	ctl_bluetooth=Bluetooth(led)
	pause()
def telegram(bot):
    bot.infinity_polling()
def intruso(bot,app):
	ctlpir=Movimiento(bot,app)
	ctlpir.run()
def sensorTemp(bot,app):
	ctlTempHum=TemperaturaHumedad(bot,app)
	ctlTempHum.run()

# Funciones para controlar debug
def debug2():
	while(True):
		print("Hilo 1")
		sleep(5)
def debug():
	while True:
		print("Hilo 2")
		sleep(5)
	
# Main para inicializar la Raspberry y sus servicios
if __name__=="__main__":
	print("Iniciando ejecución")
	led=LED(13)
	led_bomba=LED(21)
	bot=getServiceBot(led)
	ctlShow=LightShow(bot,app)
	ctlAsistente=AsistenteVirtual(bot,app)
	ctlGoogleAssistant=GoogleAssistant(bot,app)
	ctlBomba=Bomba(bot,app,led_bomba)
	ctlLedHabitacion=LedHab(app,led)
	t1=Thread(target=bluetooth_connection,args=(led,))
	t2=Thread(target=telegram,args=(bot,))
	t3=Thread(target=intruso,args=(bot,app,))
	t4=Thread(target=sensorTemp,args=(bot,app,))
	t0=Thread(target=debug)
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	app.run(host="0.0.0.0", port = "3000")
	app.add_url_rule('/favicon.ico',
                 redirect_to=url_for('static', filename='./piHomeDashboard/static/images/icons/favicon.ico'))