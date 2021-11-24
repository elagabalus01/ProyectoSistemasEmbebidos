from threading import Thread
from subprocess import Popen
from flask import jsonify
class GoogleAssistant():
    def __init__(self,bot,app):
        self.currentProcess=None
        self.activo=0
        @bot.message_handler(commands=["googleassistant"])
        def activar_asistente(message):
            Thread(target=self.activarAsistenteGoogle).start()
        @bot.message_handler(commands=["apagarasistente"])
        def desactivar_asistente(message):
            self.desactivarAsistenteGoogle()

        @app.route('/api/google', methods=['GET', 'POST'])
        def dash_google():
            try:
                data = dict()
                data['google'] = self.activo
                return jsonify(data)
            except Exception as e:
                print (e)
                return jsonify({"data":"Oops Looks like api is not correct"})

        @app.route('/api/accion/google', methods=['GET', 'POST'])
        def accion_google():
            try:
                if self.activo==0:
                    Thread(target=self.activarAsistenteGoogle).start()
                else:
                    self.desactivarAsistenteGoogle()
                data={'status_google':True}
                return jsonify(data)
            except Exception as e:
                print (e)
                return jsonify(data={'status_google':False})

    def activarAsistenteGoogle(self):
        self.activo=1
        command="/home/pi/env/bin/python -u /home/pi/GassistPi/src/main.py --project_id commanding-time-330120 --device_model_id commanding-time-330120-googleassistant-fse-4psaid"
        self.currentProcess=Popen(command.split())
    
    def desactivarAsistenteGoogle(self):
        if self.currentProcess!=None:
            self.currentProcess.terminate()
            self.currentProcess=None
            self.activo=0
