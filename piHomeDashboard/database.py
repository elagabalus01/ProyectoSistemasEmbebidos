# Importación de biblioteca
import mysql.connector

# Clase de base de datos, se establecen funciones de la clase
class db:
    
    # Inicialización de usuario, conexión a la base de datos
    def __init__(self, user, host, password, database):
        try:
            self.db = mysql.connector.connect(user=user, host=host, password=password, database=database)
            self.cursor = self.db.cursor()
            print ('[result] Database connected!')
            
        except Exception as e:
            print ('[error] error connecting database!')
            print(e)

    # Función para obtener usuario
    def user(self, username, api):
        try:
            query = "select * from users where username='{}' and api_key='{}'".format(username, api)
            self.cursor.execute(query)
            output = self.cursor.fetchall()
            return output[0]
        except Exception as e:
            print('[error] ' + e)

    # Función para obtener apikey
    def get_apikeys(self):
        query = 'select api_key from users'
        self.cursor.execute(query)
        output = self.cursor.fetchall()
        dummy = []
        for api in output:
            dummy.append(api[0])
        return dummy

    # Función para agregar usuario a base de datos
    def add_user(self, username, password, first_name, last_name, email, phone_number, api_key):  
        try:
            query = "insert into users (username, password, first_name, last_name, email, phone_number, last_login, api_key) values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', now(), '{6}');".format(username, password, first_name, last_name, email, phone_number, api_key)
            self.cursor.execute(query)
            self.db.commit()
            return "success"
        except Exception as e:
            print( e)