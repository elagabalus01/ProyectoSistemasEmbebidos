"""Google Cloud Speech"""
import argparse
import locale
import logging
import os

from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
import aiy.voice.tts

#Función para inicializar valores por defecto
def get_hints(language_code):
	if language_code.startswith('es_'):
    	return ('prende la luz',
            	'apaga la luz',
            	'parpadea la luz', 'reproduce canción',
            	'adiós',
            	'repite después de mí')
	return None

#Función para determinar lenguaje
def locale_language():
	language, _ = locale.getdefaultlocale()
	return language

#Función main para hacer reconocimiento de voz
def main():
	logging.basicConfig(level=logging.DEBUG)

	parser = argparse.ArgumentParser(description='Assistant service example.')
	parser.add_argument('--language', default=locale_language())
	args = parser.parse_args()

	logging.info('Initializing for language %s...', args.language)
	hints = get_hints(args.language)
	client = CloudSpeechClient()
	with Board() as board:
    	while True:
        	if hints:
            	logging.info('Di algo, por ejemplo %s.' % ', '.join(hints))
        	else:
            	logging.info('Di algo.')
        	text = client.recognize(language_code=args.language,
                                	hint_phrases=hints)
        	if text is None:
            	logging.info('No has dicho nada.')
            	continue

        	logging.info('Tu dijiste: "%s"' % text)
        	text = text.lower()
        	if 'prende la luz' in text:
            	aiy.voice.tts.say(text.replace('light turned on', '', 1))
            	board.led.state = Led.ON
        	elif 'apaga la luz' in text:
            	board.led.state = Led.OFF
            	aiy.voice.tts.say(text.replace('light turned off', '', 1))
        	elif 'parpadea la luz' in text:
            	board.led.state = Led.BLINK
        	# Our new command:
        	elif 'reproduce canción' in text:
            	os.system('vlc /home/pi/stay.mp3')
        	if 'repite después de mí' in text:
            	# Remove "repeat after me" from the text to be repeated
            	to_repeat = text.replace('repeat after me', '', 1)
            	aiy.voice.tts.say(to_repeat)
        	elif 'adiós' in text:
            	aiy.voice.tts.say(text.replace('goodbye', '', 1))
            	break

if __name__ == '__main__':
	main