class Bomba():
	def __init__(self,bot,led3):
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
