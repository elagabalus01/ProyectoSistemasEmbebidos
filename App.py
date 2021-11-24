'''
El progama que controla el hardware de las raspberry
'''
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
def bluetooth_connection(led):
	ctl_bluetooth=Bluetooth(led)
	pause()
def debug2():
	while(True):
		print("Hilo 1")
		sleep(5)
def debug():
	while True:
		print("Hilo 2")
		sleep(5)
def telegram(bot):
    bot.infinity_polling()
def intruso(bot,app):
	ctlpir=Movimiento(bot,app)
	ctlpir.run()
def sensorTemp(bot,app):
	ctlTempHum=TemperaturaHumedad(bot,app)
	ctlTempHum.run()

'''
def run_server(app):
	app.run(host="0.0.0.0", port = "80", debug=True)
'''
#def show_luces(bot):
#	ctlShow=LightShow(bot)
	
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
	#t5=Thread(target=run_server,args=(app,))
	t0=Thread(target=debug)
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	#t0.start()
	app.run(host="0.0.0.0", port = "3000")


