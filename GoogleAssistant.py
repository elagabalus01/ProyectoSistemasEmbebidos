# Importación de bibliotecas
from threading import Thread
from subprocess import Popen
from flask import jsonify

# Clase Google assistant, se establecen servicios de la clase
class GoogleAssistant():

    # Función de inicialización de la clase de Google assistant
    def __init__(self,bot,app):
        self.currentProcess=None
        self.activo=0

        # Funciones definidas para bot
        @bot.message_handler(commands=["googleassistant"])
        def activar_asistente(message):
            bot.send_message("1320071778",'''Con el asistente de Google encencidido se puede disfrutar de comandos de voz originales de Google:
    -> ¿Cómo está el clima?
    -> Dame una receta de cocina
    -> ¿Cómo está el clima?
    -> ¡Todo lo que tu desees saber en tiempo real!''')
            Thread(target=self.activarAsistenteGoogle).start()
        @bot.message_handler(commands=["apagargoogleassistant"])
        def desactivar_asistente(message):
            bot.send_message("1320071778","Se apagó asistente de Google")
            self.desactivarAsistenteGoogle()

        # Obtención del estado del asistente de Google
        @app.route('/api/google', methods=['GET', 'POST'])
        def dash_google():
            try:
                data = dict()
                data['google'] = self.activo
                return jsonify(data)
            except Exception as e:
                print (e)
                return jsonify({"data":"Oops Looks like api is not correct"})

        # Ejecución del asistente de Google por medio de WEB
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

    # Función para iniciar asistente de Google
    def activarAsistenteGoogle(self):
        self.activo=1
        command="/home/pi/env/bin/python -u /home/pi/GassistPi/src/main.py --project_id commanding-time-330120 --device_model_id commanding-time-330120-googleassistant-fse-4psaid"
        self.currentProcess=Popen(command.split())
    
    # Función para desactivar el asistente de Google
    def desactivarAsistenteGoogle(self):
        if self.currentProcess!=None:
            self.currentProcess.terminate()
            self.currentProcess=None
            self.activo=0
