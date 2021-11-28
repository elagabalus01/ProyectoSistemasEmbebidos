"""Google Cloud Speech"""

# Importación de bibliotecas
import locale
import logging
import os
from threading import Thread
from subprocess import Popen
from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
import aiy.voice.tts
from flask import jsonify
from subprocess import Popen,call,PIPE
from Constantes import Constantes
from gpiozero import LED

# Función para inicializar valores por defecto
def get_hints(language_code):
    if language_code.startswith('es_'):
        return ('prende la luz',
        'apaga la luz',
        'parpadea la luz', 'reproduce canción',
        'adiós',
        'repite después de mí')
    return None

# Función para determinar lenguaje
def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

# Clase asistente virtual, se establecen servicios de la clase
class AsistenteVirtual():
    
    # Inicialización de clase asistente virtual
    def __init__(self,bot,app,led):
        self.led=led
        sufix=['sudo','python']
        self.path_script_fiesta=sufix+'/home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/stay.mp3'.split(' ')
        self.sudo_password = 'raspberry'
        self.process=None
        self.activo=0
        @bot.message_handler(commands=['asistentevirtual'])
        def activar_reconocimiento(message):
            bot.send_message(Constantes.chat_id(),'''Con el asistente de voz encendido puedes personalizar tus peticiones, algunas son:
    -> prende la luz
    -> apaga la luz
    -> parpadea la luz
    -> reproduce canción
    -> activa modo fiesta
    -> repite después de mí
    -> termina canción''')
            Thread(target=self.activar_asistente).start()

        # Función para obtener información
        @app.route('/api/asistentevirtual', methods=['GET', 'POST'])
        def dash_asistente():
            try:
                data = dict()
                data['asistente'] = self.activo
                return jsonify(data)
            except Exception as e:
                print (e)
                return jsonify({"data":"Oops Looks like api is not correct"})

        # Función para correr comando desde WEB
        @app.route('/api/accion/asistentevirtual', methods=['GET', 'POST'])
        def accion_asistente():
            try:
                if self.activo==0:
                    Thread(target=self.activar_asistente).start()
                data={'status_asistente':True}
                return jsonify(data)
            except Exception as e:
                print (e)
                return jsonify(data={'status_asistente':False})
    
    # Función para activar asistente
    def activar_asistente(self):
        self.activo=1
        logging.basicConfig(level=logging.DEBUG)
        language=locale_language()
        hints = get_hints(language)
        client = CloudSpeechClient()
        with Board() as board:
            while True:
                if hints:
                    logging.info('Di algo, por ejemplo %s.' % ', '.join(hints))
                else:
                    logging.info('Di algo.')
                text = client.recognize(language_code=language,
                                hint_phrases=hints)
                if text is None:
                    logging.info('No has dicho nada.')
                    continue

                logging.info('Tu dijiste: "%s"' % text)
                text = text.lower()
                if 'prende la luz' in text:
                    aiy.voice.tts.say(text.replace('light turned on', '', 1))
                    self.led.on()
                elif 'apaga la luz' in text:
                    self.led.off()
                    aiy.voice.tts.say(text.replace('light turned off', '', 1))
                elif 'parpadea la luz' in text:
                    self.led.blink()
                elif 'reproduce canción' in text:
                    self.process=Popen(['vlc','/home/pi/stay.mp3'])
                elif 'activa modo fiesta' in text:
                    self.process=Popen(self.path_script_fiesta,stdin=PIPE,stderr=PIPE,universal_newlines=True)
                    sudo_prompt = self.process.communicate(self.sudo_password + '\n')[1]
                elif 'repite después de mí' in text:
                    to_repeat = text.replace('repeat after me', '', 1)
                    aiy.voice.tts.say(to_repeat)
                elif 'termina canción' in text:
                    if self.process != None:
                        self.process.terminate()
                        self.process=None
                elif 'adiós' in text:
                    aiy.voice.tts.say(text.replace('goodbye', '', 1))
                    self.activo=0
                    self.led.off()
                    break

# Función main para hacer reconocimiento de voz
def main():
    pass

if __name__ == '__main__':
    main