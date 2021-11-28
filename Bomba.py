# Importación de bibliotecas
from flask import jsonify
from Constantes import Constantes

# Clase bomba, se establecen servicios de la clase
class Bomba():

    # Función de inicialización de la clase bomba
    def __init__(self,bot,app,led3):

        # Se definen comandos utilizados por el bot
        @bot.message_handler(commands=["enciendebomba"])
        def encendido(message):
            led3.on()
            bot.send_message(Constantes.chat_id(),"Bomba encendida")
        
        @bot.message_handler(commands=["apagabomba"])
        def apagado(message):
            led3.off()
            bot.send_message(Constantes.chat_id(),"Bomba apagada")
        
        # Se define la obtención de información de la bomba
        @app.route('/api/bomba', methods=['GET', 'POST'])
        def dash_bomba():
            try:
                data = dict()
                data['bomba'] = led3.value
                return jsonify(data)
            except Exception as e:
                print (e)
                return jsonify({"data":"Oops Looks like api is not correct"})
        
        # Ejecución de función a través de WEB
        @app.route('/api/accion/bomba', methods=['GET', 'POST'])
        def accion_bomba():
            try:
                if led3.value==1:
                    led3.value=0
                else:
                    led3.value=1
                data={'status_bomba':True}
                return jsonify(data)
            except Exception as e:
                print (e)
                return jsonify(data={'status_bomba':False})