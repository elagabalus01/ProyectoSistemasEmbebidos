# Importación de bibliotecas
import os
from gpiozero import MotionSensor
import telebot
from flask import jsonify
import time

# Clase Movimiento para sensor PIR, se establecen servicios de la clase
class Movimiento():
    def __init__(self,bot,app):
        self.pir=MotionSensor(4)
        self.bot=bot
        self.intruso=False
        self.detecta_intruso=False

        @bot.message_handler(commands=['modointruso'])
        def activar_intruso(message):
            self.detecta_intruso= not self.detecta_intruso
            if(self.detecta_intruso):
                self.bot.send_message("1320071778","Modo intruso activado")
            else:
                self.bot.send_message("1320071778","Modo intruso desactivado")

        @app.route('/api/intruso', methods=['GET', 'POST'])
        def dash_movimiento():
            try:
                data = dict()
                data['intruso'] = self.intruso
                return jsonify(data)
            except Exception as e:
                print (e)
                return jsonify({"data":"Oops Looks like api is not correct"})

    def run(self):
        while True:
            if(self.detecta_intruso):
                self.pir.wait_for_motion()
                self.intruso=True
                print("Se detectó intruso")
                self.bot.send_message("1320071778","Se detectó intruso")
                self.pir.wait_for_no_motion()
                print("Se retiró intruso")
                self.bot.send_message("1320071778","Se retiró intruso")
                self.intruso=False

