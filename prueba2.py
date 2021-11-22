import os
import telebot
def getServiceBot(led):
    API_TOKEN= '2044324567:AAE6IWSJ8VQILqN5WlZQ-L_c6va9po0twuI'
    bot=telebot.TeleBot(API_TOKEN)

    # Función de comando para apagar led
    @bot.message_handler(commands=["apaga"])
    def turn_off(message):
        led.off()
        bot.reply_to(message,"se apaga led")

    # Función de comando para encender led
    @bot.message_handler(commands=["enciende"])
    def turn_on(message):
        led.on()
        bot.reply_to(message,"se enciende led")
    return bot
if __name__=="__main__":
    from gpiozero import LED
    led= LED(13)
    bot=getServiceBot(led)
    bot.infinity_polling()
