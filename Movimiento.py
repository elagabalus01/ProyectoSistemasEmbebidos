# Importación de bibliotecas
import os
from gpiozero import MotionSensor
import telebot
from flask import jsonify
import time
from Constantes import Constantes

# Clase Movimiento para sensor PIR, se establecen servicios de la clase
class Movimiento():

    # Función de inicialización para clase Movimiento
    def __init__(self,bot,app):
        self.pir=MotionSensor(4)
        self.bot=bot
        self.intruso=False
        self.detecta_intruso=False

        # Comando que será cachado por bot
        @bot.message_handler(commands=['modointruso'])
        def activar_intruso(message):
            self.detecta_intruso= not self.detecta_intruso
            if(self.detecta_intruso):
                self.bot.send_message(Constantes.chat_id(),"Modo intruso activado")
            else:
                self.bot.send_message(Constantes.chat_id(),"Modo intruso desactivado")

        # Obtención de información de modo intruso
        @app.route('/api/intruso', methods=['GET', 'POST'])
        def dash_movimiento():
            try:
                data = dict()
                data['intruso'] = self.intruso
                data['detecta_intruso'] = self.detecta_intruso
                return jsonify(data)
            except Exception as e:
                print (e)
                return jsonify({"data":"Oops Looks like api is not correct"})

        # Acción intruso
        @app.route('/api/accion/intruso', methods=['GET', 'POST'])
        def accion_intruso():
            try:
                if self.detecta_intruso==1:
                    self.detecta_intruso=0
                    self.bot.send_message(Constantes.chat_id(),"Modo intruso desactivado")
                else:
                    self.detecta_intruso=1
                    self.bot.send_message(Constantes.chat_id(),"Modo intruso activado")
                data={'status_intruso':True}
                return jsonify(data)
            except Exception as e:
                print (e)
                return jsonify(data={'status_intruso':False})
    
    # Función de ejecución para clase Movimiento
    def run(self):
        while True:
            if(self.detecta_intruso):
                self.pir.wait_for_motion()
                self.intruso=True
                print("Se detectó intruso")
                self.bot.send_message(Constantes.chat_id(),"Se detectó intruso")
                self.pir.wait_for_no_motion()
                print("Se retiró intruso")
                self.bot.send_message(Constantes.chat_id(),"Se retiró intruso")
                self.intruso=False

