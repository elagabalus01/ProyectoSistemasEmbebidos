import os
from gpiozero import MotionSensor
import telebot
from flask import jsonify
class Movimiento():
    def __init__(self,bot,app):
        self.pir=MotionSensor(4)
        self.bot=bot
        self.intruso=False
        @app.route('/api/intruso', methods=['GET', 'POST'])
        def dash_movimiento():
            try:
                #this part is hard coded so remove after fixing the issue
                data = dict()
                data['intruso'] = self.intruso
                return jsonify(data)
            except Exception as e:
                print (e)
                return jsonify({"data":"Oops Looks like api is not correct"})
    def run(self):
        # Si se detecta movimiento se imprime en consola, se manda mensaje a telegram y se enciende el led
        while True:
            self. pir.wait_for_motion()
            self.intruso=True
            print("Se detectó intruso")
            self.bot.send_message("1320071778","Se detectó intruso")
            self.pir.wait_for_no_motion()
            print("Se retiró intruso")
            self.bot.send_message("1320071778","Se retiró intruso")
            self.intruso=False

