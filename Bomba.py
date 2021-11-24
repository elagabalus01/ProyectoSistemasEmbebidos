from flask import jsonify
class Bomba():
    def __init__(self,bot,app,led3):
        #Función de comando para encender la bomba
        @bot.message_handler(commands=["enciendebomba"])
        def encendido(message):
            #motor_on(channel)
            led3.on()
            #bot.reply_to(message,"Se enciende bomba")
            bot.send_message("1320071778","Bomba encendida")
            #GPIO.cleanup()
        
        # Función de comando para apagar la bomba
        @bot.message_handler(commands=["apagabomba"])
        def apagado(message):
            #motor_off(channel)
            led3.off()
            #bot.reply_to(message,"Se apaga bomba")
            bot.send_message("1320071778","Bomba apagada")
            #GPIO.cleanup()
        
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