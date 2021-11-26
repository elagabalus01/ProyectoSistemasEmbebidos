# Importación de bibliotecas
import os
from threading import Thread
import signal
from subprocess import Popen,call,PIPE
from flask import jsonify
import time

# Clase LightShow, se establecen servicios de la clase
class LightShow():

  # Función para inicializar clase LightShow
  def __init__(self,bot,app):
    sufix=['sudo','python']
    self.path_script_show=sufix+'/home/pi/lightshowpi/py/hardware_controller.py --state=flash'.split(' ')
    self.path_script_music=sufix+'/home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/stay.mp3'.split(' ')
    self.path_script_prepost=sufix+'/home/pi/lightshowpi/py/prepostshow.py'.split(' ')
    sudoPassword = 'raspberry'
    command = 'mount -t vboxsf lightshowpi /home/pi/lightshowpi'
    self.running=False
    self.currentPID=-1
    self.currentProcess=None
    self.activo=0
    
    # Funciones para comandos del bot
    @bot.message_handler(commands=["flash"])
    def flash(message):
      bot.send_message("1320071778","Iniciando flash")
      Thread(target=self.flash_thread).start()
    
    @bot.message_handler(commands=["show"])
    def show(message):
      bot.send_message("1320071778","Iniciando show")
      Thread(target=self.show_thread).start()

    @bot.message_handler(commands=["musica"])
    def musica(message):
      bot.send_message("1320071778","Reproduciendo música")
      Thread(target=self.musica_thread).start()

    # Obtención del estado de modo fiesta
    @app.route('/api/modofiesta', methods=['GET', 'POST'])
    def dash_fiesta():
      try:
        data = dict()
        print(self.activo)
        data['modofiesta'] = self.activo
        return jsonify(data)
      except Exception as e:
        print (e)
        return jsonify({"data":"Oops Looks like api is not correct"})

    # Ejecución de modo fiesta vía WEB
    @app.route('/api/accion/modofiesta', methods=['GET', 'POST'])
    def activar_fiesta():
      try:
        if self.activo==0:
          Thread(target=self.musica_thread).start()
        data={'status_modofiesta':True}
        return jsonify(data)
      except Exception as e:
        print (e)
        return jsonify(data={'status_modofiesta':False})
      
  # Hilos que cooperan con la ejecución de código externo para los leds
  def show_thread(self):
    p=Popen(self.path_script_prepost,stdin=PIPE,stderr=PIPE,universal_newlines=True)
    sudo_prompt = p.communicate(sudo_password + '\n')[1]

  def musica_thread(self):
    self.activo=1
    time.sleep(5)
    self.activo=0
    p=Popen(self.path_script_music,stdin=PIPE,stderr=PIPE,universal_newlines=True)
    sudo_prompt = p.communicate(sudo_password + '\n')[1]

  def flash_thread(self):
    p=Popen(self.path_script_show,stdin=PIPE,stderr=PIPE,universal_newlines=True)
    sudo_prompt = p.communicate(sudo_password + '\n')[1]