import telebot
from gpiozero import LED
led=LED(13)
#def getServiceBot(led):
API_TOKEN='2044324567:AAE6IWSJ8VQILqN5WlZQ-L_c6va9po0twuI'
bot=telebot.TeleBot(API_TOKEN)
# Función de comando help
@bot.message_handler(commands=['help'])
def send_help(message):
    print("se envia mensaje")
    bot.reply_to(message,"¿Necesitas ayuda?")

# Función de comando start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Hola, dime tu nombre")
# Función para enceder el led
@bot.message_handler(commands=['enceder'])
def send_encender(message):
    print("Se va a enceder el led")
    led.on()
    bot.reply_to(message,"Led encendido")
# Función para enceder el led
@bot.message_handler(commands=['debug'])
def send_debug(message):
    print("Prueba")
    raise Exception("Error")
    bot.reply_to(message,"Debug")
#return bot
#if __name__=="__main__":
    
bot.infinity_polling()
    
