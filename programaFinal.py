from gpiozero import LED, Button, TrafficLights, MotionSensor
from bluedot import BlueDot
from time import sleep
from signal import pause
from collections import deque
import os
import telebot
import threading as th
import math
import Adafruit_DHT
import RPi.GPIO as GPIO

global leds
button=Button(2)
leds=[0, 0, 1]

led = LED(17)
led2 = LED(21)
#channel = 11
led3 = LED(11)
led4 = LED(20)

pir = MotionSensor(4)

lights = TrafficLights(26, 19, 13)

sensor=Adafruit_DHT.DHT11
gpio = 27

tmpTemperatura = 0
tmpHumedad = 0

#bd = BlueDot()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.setup(channel, GPIO.OUT)

sudoPassword = 'raspberry'
command = 'mount -t vboxsf lightshowpi /home/pi/lightshowpi'

def pool():
  bot.infinity_polling()

# Bomba de agua
def motor_on(pin):
	GPIO.output(pin, GPIO.HIGH)

def motor_off(pin):
	GPIO.output(pin, GPIO.LOW)

# Función de thread para ejecutar hardware_controller.py con flash
def flash_thread():
  os.system("sudo python /home/pi/lightshowpi/py/hardware_controller.py --state=flash")

# Función de thread para ejecutar prepostshow
def show_thread():
  os.system("sudo python /home/pi/lightshowpi/py/prepostshow.py")

# Función de thread para reproducir música y encender leds
def musica_thread():
  os.system("sudo python /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/lightshowpi/stay.mp3")


'''
# Luces con BlueDot
def traffic_light_sequence():
	global leds
	while True:
		yield leds
		sleep(2)
		leds=leds[1:]+leds[:1]
		yield leds
		sleep(2)
		leds=leds[1:]+leds[:1]
		yield leds
		sleep(2)
		leds=leds[1:]+leds[:1]

def control_p_value():
	print("Peaton")
	global leds
	leds=[1,0,0]
	sleep(2)

lights.source = traffic_light_sequence()
bd.when_pressed = control_p_value

pause()
'''

API_TOKEN= '2015963181:AAFb58Nj83D5o8o11EHI-QIPzLhRGSlnAR4'
bot=telebot.TeleBot(API_TOKEN)

# Función de comando para apagar led
@bot.message_handler(commands=["apagaLED"])
def turn_off(message):
    led.off()
    bot.reply_to(message,"se apaga led")

# Función de comando para encender led
@bot.message_handler(commands=["enciendeLED"])
def turn_on(message):
    led.on()
    bot.reply_to(message,"se enciende led")

# Función de comando para encender la bomba
@bot.message_handler(commands=["enciendeBomba"])
def encendido(message):
	#motor_on(channel)
	led3.on()
	#bot.reply_to(message,"Se enciende bomba")
	bot.send_message("934906619","Bomba encendida")
	#GPIO.cleanup()

# Función de comando para apagar la bomba
@bot.message_handler(commands=["apagaBomba"])
def apagado(message):
	#motor_off(channel)
	led3.off()
	#bot.reply_to(message,"Se apaga bomba")
	bot.send_message("934906619","Bomba apagada")
	#GPIO.cleanup()

# Función de comando para ejecutar hardware_controller.py con flash
@bot.message_handler(commands=["flash"])
def flash(message):
  bot.send_message("934906619","Iniciando flash")
  th.Thread(target=flash_thread).start()

# Función de comando para reproducir música y encender leds
@bot.message_handler(commands=["musica"])
def musica(message):
  bot.send_message("934906619","Reproduciendo música")
  Thread(target=musica).start()

# Función de comando para ejecutar prepostshow
@bot.message_handler(commands=["show"])
def show(message):
  bot.send_message("934906619","Iniciando show")
  th.Thread(target=show_thread).start()

# Función de comando para mostrar temperatura
@bot.message_handler(commands=["temperatura"])
def temperatura(message):
  bot.send_message("934906619","La temperatura es: "+str(math.trunc(tmpTemperatura))+"°C")

# Función de comando para mostrar humedad
@bot.message_handler(commands=["humedad"])
def humedad(message):
  bot.send_message("934906619","La humedad es: "+str(math.trunc(tmpHumedad))+"%")


#bot.infinity_polling()

# Si se detecta movimiento se imprime en consola, se manda mensaje a telegram y se enciende el led
while True:
    pir.wait_for_motion()
    print("Se detectó intruso")
    bot.send_message("934906619","Se detectó intruso")
    led2.on()
    led4.on()
    pir.wait_for_no_motion()
    led2.off()
    led4.off()

# LightShowPi
#th.Thread(target=pool).start()

# Sensor de Temperatura
#th.Thread(target=pool).start()

while True:
  humedad, temperatura = Adafruit_DHT.read(sensor, gpio)
  if humedad is not None and temperatura is not None:
    print('Temperatura={0:0.1f}°C  Humedad={1:0.1f}%'.format(temperatura, humedad))
  else:
    print('Falló en tomar lectura')
  if humedad is not None:
    tmpHumedad = humedad
  if temperatura is not None:
    tmpTemperatura = temperatura
  time.sleep(5)

bot.infinity_polling()
