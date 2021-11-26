# Importación de biblioteca
from flask import jsonify

# Clase bomba, se establecen servicios de la clase
class Bomba():
    def __init__(self,bot,app,led3):
        @bot.message_handler(commands=["enciendebomba"])
        def encendido(message):
            led3.on()
            bot.send_message("1320071778","Bomba encendida")
        
        @bot.message_handler(commands=["apagabomba"])
        def apagado(message):
            led3.off()
            bot.send_message("1320071778","Bomba apagada")
        
        @app.route('/api/bomba', methods=['GET', 'POST'])
        def dash_bomba():
            try:
                data = dict()
                data['bomba'] = led3.value
                return jsonify(data)
            except Exception as e:
                print (e)
                return jsonify({"data":"Oops Looks like api is not correct"})
        
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