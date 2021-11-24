from threading import Thread
from subprocess import Popen
class GoogleAssistant():
	def __init__(self,bot):
		self.currentProcess=None
		@bot.message_handler(commands=["googleassistant"])
		def activar_asistente(message):
			Thread(target=self.activarAsistenteGoogle).start()
		@bot.message_handler(commands=["apagarasistente"])
		def desactivar_asistente(message):
			self.desactivarAsistenteGoogle()
	
	def activarAsistenteGoogle(self):
		command="/home/pi/env/bin/python -u /home/pi/GassistPi/src/main.py --project_id commanding-time-330120 --device_model_id commanding-time-330120-googleassistant-fse-4psaid"
		self.currentProcess=Popen(command.split())
	
	def desactivarAsistenteGoogle(self):
		if self.currentProcess!=None:
			self.currentProcess.terminate()
			self.currentProcess=None
			
		
		
			
			
		
