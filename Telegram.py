# Importación de bibliotecas
import os
import telebot
from Constantes import Constantes

# Inicialización de bot
def getServiceBot(led):
    API_TOKEN= '2044324567:AAE6IWSJ8VQILqN5WlZQ-L_c6va9po0twuI'
    bot=telebot.TeleBot(API_TOKEN)
    bot.send_message(Constantes.chat_id(),Constantes.mensaje_inicio(), parse_mode= 'Markdown')
    

    # Función de comando para apagar led
    @bot.message_handler(commands=["apaga"])
    def turn_off(message):
        led.off()
        bot.reply_to(message,"Se apaga led")

    # Función de comando para encender led
    @bot.message_handler(commands=["enciende"])
    def turn_on(message):
        led.on()
        bot.reply_to(message,"Se enciende led")

    # Función de comando start
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(Constantes.chat_id(),Constantes.mensaje_inicio(), parse_mode= 'Markdown')
    
    return bot

# Función main para bot
if __name__=="__main__":
    from gpiozero import LED
    led= LED(13)
    bot=getServiceBot(led)
    bot.infinity_polling()
