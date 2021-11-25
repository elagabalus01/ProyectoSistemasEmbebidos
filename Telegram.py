import os
import telebot
def getServiceBot(led):
    API_TOKEN= '2044324567:AAE6IWSJ8VQILqN5WlZQ-L_c6va9po0twuI'
    bot=telebot.TeleBot(API_TOKEN)

    bot.send_message("1320071778",'''🌏🏠🤖☑ **Bienvenido a PiHome ☑🤖🏠🌏 
        
Hay algunas funciones que sirven tanto en Telegram, Web y Bluetooth, por defecto la mayoría se encuentra disponible en Telegram, las disponibles en Web y Bluetooth se indican con (BT, o WEB).
        
Los comandos disponibles son:
    -> /enciende: 
    🚨 enciende la luz de la habitación. (BT, WEB).
    -> /apaga: 
    🚨 apaga la luz de la habitación. (BT, WEB).
    -> /modointruso: 
    🏃‍♀️ se habilitan o deshabilitan anuncios de intrusión. (WEB).
    -> /temperatura: 
    ⛈ se muestra la temperatura actual (WEB).
    -> /humedad: 
    💧 se muestra la temperatura actual (WEB).
    -> /enciendebomba: 
    🌻 se enciende la bomba para regar las plantas (WEB).
    -> /apagabomba: 
    🌻 se apaga la bomba para regar las plantas (WEB).
    -> /flash: 
    🚨 parpadean los leds de la habitación, uno por uno.
    -> /show: 
    🚨 parpadean los leds de la habitación, juntos.
    -> /musica: 
    🎧 parpadean los leds de acuerdo a la música (WEB, equivalente a Modo Fiesta).
    -> /asistentevirtual: 
    🤖 se habilita asistente personalizado (WEB).
    (para terminarlo es necesario que digas 'adiós')
    -> /googleassistant: 
    🤖 se habilita asistente de google (WEB).
    -> /apagargoogleassistant: 
    🤖 se deshabilita asistente de google (WEB).

Con el asistente de Google encencidido se puede disfrutar de comandos de voz originales de Google:
    -> ¿Cómo está el clima?
    -> Dame una receta de cocina
    -> ¿Cómo está el clima?
    -> ¡Todo lo que tu desees saber en tiempo real!

Con el asistente de voz encendido puedes personalizar tus peticiones, algunas son:
    -> prende la luz
    -> apaga la luz
    -> parpadea la luz
    -> reproduce canción
    -> activa modo fiesta
    -> repite después de mí
    -> termina canción

Para ver las opciones disponibles de nuevo escribe el comando /start, por lo mientras disfruta de nuestra solución IoT 😁😋**''', parse_mode= 'Markdown')
    

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
        bot.send_message("1320071778",'''🌏🏠🤖☑ **Bienvenido a PiHome ☑🤖🏠🌏 
        
Hay algunas funciones que sirven tanto en Telegram, Web y Bluetooth, por defecto la mayoría se encuentra disponible en Telegram, las disponibles en Web y Bluetooth se indican con (BT, o WEB).
        
Los comandos disponibles son:
    ->/enciende: 
    🚨 enciende la luz de la habitación. (BT, WEB).
    ->/apaga: 
    🚨 apaga la luz de la habitación. (BT, WEB).
    ->/modointruso: 
    🏃‍♀️ se habilitan o deshabilitan anuncios de intrusión. (WEB).
    ->/temperatura: 
    ⛈ se muestra la temperatura actual (WEB).
    ->/humedad: 
    💧 se muestra la temperatura actual (WEB).
    ->/enciendebomba: 
    🌻 se enciende la bomba para regar las plantas (WEB).
    ->/apagabomba: 
    🌻 se apaga la bomba para regar las plantas (WEB).
    ->/flash: 
    🚨 parpadean los leds de la habitación, uno por uno.
    ->/show: 
    🚨 parpadean los leds de la habitación, juntos.
    ->/musica: 
    🎧 parpadean los leds de acuerdo a la música (WEB, equivalente a Modo Fiesta).
    ->/asistentevirtual: 
    🤖 se habilita asistente personalizado (WEB).
    (para terminarlo es necesario que digas 'adiós')
    ->/googleassistant: 
    🤖 se habilita asistente de google (WEB).
    ->/apagargoogleassistant: 
    🤖 se deshabilita asistente de google (WEB).

Con el asistente de Google encencidido se puede disfrutar de comandos de voz originales de Google:
    -> ¿Cómo está el clima?
    -> Dame una receta de cocina
    -> ¿Cómo está el clima?
    -> ¡Todo lo que tu desees saber en tiempo real!

Con el asistente de voz encendido puedes personalizar tus peticiones, algunas son:
    -> prende la luz
    -> apaga la luz
    -> parpadea la luz
    -> reproduce canción
    -> activa modo fiesta
    -> repite después de mí
    -> termina canción

Para ver las opciones disponibles de nuevo escribe el comando /start, por lo mientras disfruta de nuestra solución IoT 😁😋**''', parse_mode= 'Markdown')
    
    return bot
if __name__=="__main__":
    from gpiozero import LED
    led= LED(13)
    bot=getServiceBot(led)
    bot.infinity_polling()
