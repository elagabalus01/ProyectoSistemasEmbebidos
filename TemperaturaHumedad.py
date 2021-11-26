# importación de bibliotecas
import Adafruit_DHT
import time
import telebot
import math
from threading import Thread
from flask import jsonify

# Clasee para 
class TemperaturaHumedad():

  # función de inicialización de clase TemperaturaHumedad
  def __init__(self,bot,app):
    self.sensor=Adafruit_DHT.DHT11
    self.gpio=23
    self.tmpTemperatura = 0
    self.tmpHumedad = 0

    # Función de comando para mostrar temperatura
    @bot.message_handler(commands=["temperatura"])
    def temperatura(message):
      bot.send_message("1320071778","La temperatura es: "+str(math.trunc(self.tmpTemperatura))+"°C")

    # Función de comando para mostrar humedad	
    @bot.message_handler(commands=["humedad"])
    def humedad(message):
      bot.send_message("1320071778","La humedad es: "+str(math.trunc(self.tmpHumedad))+"%")
    print("Agregando rutas de flask")

    # Obtención de información de temperatura
    @app.route('/api/temperatura', methods=['GET', 'POST'])
    def dash_temperatura():
      try:
        data = dict()
        data['temperatura'] = self.tmpTemperatura
        return jsonify(data)
      except Exception as e:
        print (e)
        return jsonify({"data":"Oops Looks like api is not correct"})
      
    # Obtención de información de humedad
    @app.route('/api/humedad', methods=['GET', 'POST'])
    def dash_humedad():
      try:
        data = dict()
        data['humedad'] = self.tmpHumedad
        return jsonify(data)
      except Exception as e:
        print (e)
        return jsonify({"data":"Oops Looks like api is not correct"})

  # Función de ejecución para sensor temperatura-humedad
  def run(self):
    while True:
      self.humedad, self.temperatura = Adafruit_DHT.read(self.sensor, self.gpio)
      if self.humedad is not None and self.temperatura is not None:
        print('Temperatura={0:0.1f}°C  Humedad={1:0.1f}%'.format(self.temperatura, self.humedad))
      else:
        print('Falló en tomar lectura')
      if self.humedad is not None:
        self.tmpHumedad = self.humedad
      if self.temperatura is not None:
        self.tmpTemperatura = self.temperatura
      time.sleep(5)
