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
from Lightshow import LightShow
from AsistenteVirtual import AsistenteVirtual
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
def intruso(bot):
	pir=MotionSensor(4)
	while True:
		pir.wait_for_motion()
		print("Se detectó intruso")
		bot.send_message("1320071778","Se detectó intruso")
		pir.wait_for_no_motion()
		print("Se retiró intruso")
		bot.send_message("1320071778","Se retiró intruso")
def sensorTemp(bot):
	ctlTempHum=TemperaturaHumedad(bot)
	ctlTempHum.run()

	
#def show_luces(bot):
#	ctlShow=LightShow(bot)
	
if __name__=="__main__":
	print("Iniciando ejecución")
	led= LED(13)
	bot=getServiceBot(led)
	ctlShow=LightShow(bot)
	ctlAsistente=AsistenteVirtual(bot)
	t1=Thread(target=bluetooth_connection,args=(led,))
	t2=Thread(target=telegram,args=(bot,))
	t3=Thread(target=intruso,args=(bot,))
	t4=Thread(target=sensorTemp,args=(bot,))
	t0=Thread(target=debug)
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t0.start()


