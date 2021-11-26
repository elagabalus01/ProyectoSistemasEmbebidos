from flask import Flask, render_template, jsonify, redirect, request
import json, base64
from random import choice
from datetime import datetime
import piHomeDashboard.person as person
import piHomeDashboard.database as database
import os, binascii

app = Flask(__name__)

# Lee el archivo de configuración con la dirección y credenciales
# para aceeder a la base de datos
with open('config.json','r') as file:
    env=json.loads(file.read())
mydb = database.db(env['user'],env['ip'],env['password'],env['db'])

# Variables que controlan la sesión del usuario
logged_in = {}
api_loggers = {}

# Ruta que renderiza la página de inicio de sesión
# Mediante el verbo POST realiza el inicio de sesión

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        user = person.user(request.form['username'], request.form['password'])
        if user.authenticated:
            user.session_id = str(binascii.b2a_hex(os.urandom(15)))
            logged_in[user.username] = {"object": user}
            return redirect('/overview/{}/{}'.format(request.form['username'], user.session_id))
        else:
            error = "invalid Username or Passowrd"
       
    return render_template('Login.htm', error=error)
    
# Renderiza la página de bienvenida
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.htm', title='PiHome')

# Renderiza la pantalla del dashboard
@app.route('/overview/<string:username>/<string:session>', methods=['GET', 'POST'])
def overview(username, session):
    
    global logged_in

    if username in logged_in and (logged_in[username]['object'].session_id == session):
        user = {
            "username" : username,
            "image":"/static/images/amanSingh.jpg",
            "api": logged_in[username]["object"].api,
            "session" : session
        }

        devices = [
            {"Dashboard" : "device1",
            "deviceID": "Device1"
            }
        ]
        return render_template('overview.htm', title='Overview', user=user, devices=devices)
    
    else:
        return redirect('/login')

# Renderiza la página del perfil del usuario definido en la ruta
@app.route('/profile/<string:username>/<string:session>', methods=['GET', 'POST'])
def profile(username, session):
    
    global logged_in

    if username in logged_in and (logged_in[username]['object'].session_id == session):
        user = {
            "username" : username,
            "image":"/static/images/amanSingh.jpg",
            "api": logged_in[username]["object"].api,
            "session" : session,
            "firstname": logged_in[username]["object"].first,
            "lastname": logged_in[username]["object"].last,
            "email":logged_in[username]["object"].email,
            "phone":logged_in[username]["object"].phone,
            "lastlogin":logged_in[username]["object"].last_login,
        }

        devices = [
            {"Dashboard" : "device1",
            "deviceID": "ARMS12012"
            }
        ]
        return render_template('profile.htm', title='API-Settings', user=user, devices=devices)
    
    else:
        return redirect('/login')

# Cierra sesión del usuario definido en la ruta
@app.route('/logout/<string:username>/<string:session>', methods=['GET', 'POST'])
def logout(username, session):
    
    global logged_in

    if username in logged_in and (logged_in[username]['object'].session_id == session):
        logged_in.pop(username)
        # print("logged out")
        return redirect('/')
    else:
        return redirect('/login')

# Función de prueba de la aplicación
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = "80", debug=True)
