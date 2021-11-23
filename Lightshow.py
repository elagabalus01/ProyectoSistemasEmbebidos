import os
from threading import Thread
import signal
from subprocess import Popen,call
class LightShow():
  def __init__(self,bot):
    sufix=['sudo','python']
    self.path_script_show=sufix+'/home/pi/lightshowpi/py/hardware_controller.py --state=flash'.split(' ')
    self.path_script_music=sufix+'/home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/stay.mp3'.split(' ')
    self.path_script_prepost=sufix+'/home/pi/lightshowpi/py/prepostshow.py'.split(' ')
    sudoPassword = 'raspberry'
    command = 'mount -t vboxsf lightshowpi /home/pi/lightshowpi'
    self.running=False
    self.currentPID=-1
    self.currentProcess=None
    
    # Función de comando para ejecutar hardware_controller.py con flash
    @bot.message_handler(commands=["flash"])
    def flash(message):
      bot.send_message("1320071778","Iniciando flash")
      Thread(target=self.flash_thread).start()
      
    
    # Función de comando para ejecutar prepostshow
    @bot.message_handler(commands=["show"])
    def show(message):
      bot.send_message("1320071778","Iniciando show")
      Thread(target=self.show_thread).start()

    # Función de comando para reproducir música y encender leds
    @bot.message_handler(commands=["musica"])
    def musica(message):
      bot.send_message("1320071778","Reproduciendo música")
      Thread(target=self.musica_thread).start()
      
    @bot.message_handler(commands=["terminarshow"])
    def detener(message):
      if self.currentPID!=-1 and (self.currentProcess != None):
        print(f"Proceso {self.currentPID}")
        #signal.raise_signal( signal.SIGINT )
        self.currentProcess.kill()
        os.kill(self.currentPID+1,signal.SIGKILL)
        bot.send_message("1320071778","El show ha terminado")
      else:
        bot.send_message("1320071778","No hay show de luces")
      
  # Función de thread para ejecutar prepostshow
  def show_thread(self):
    process=Popen(self.path_script_prepost)
    self.currentPID=process.pid
    self.currentProcess=process
  # Función de thread para reproducir música y encender leds
  def musica_thread(self):
    process=Popen(self.path_script_music)
    self.currentPID=process.pid
    self.currentProcess=process
    print(f"Identificador de proceso {self.currentPID}")
  # Función de thread para ejecutar hardware_controller.py con flash
  def flash_thread(self):
    process=Popen(self.path_script_show)
    self.currentPID=process.pid
    self.currentProcess=process

  
