#!/usr/bin/env python
'''
Base de datos de Tienda Lissa con interfaz html
---------------------------
Autor: Arrascaeta Nahuel
Versión: 1.0
 
Descripción:
Se utiliza Flask para crear un WebServer que registra los datos de ventas, compras y fiados de Tienda Lissa.

Ejecución: Lanzar el programa y abrir en un navegador la siguiente dirección URL
http://127.0.0.1:5000/
'''
__author__ = "Arrascaeta Nahuel"
__email__ = "nahuelarrascaeta22@gmail.com"
__version__ = "1.0"

#Librerías
import traceback
import io
#import sys
import os
from datetime import datetime
#from datetime import datetime, timedelta
#Matplotlib para realizar un balance general de ventas y compras
import matplotlib.pyplot as plt
#Flask
from flask import Flask, request, jsonify, render_template, Response, make_response, redirect, url_for
# import requests
# Archivos míos
import tienda_lissa_venta
import tienda_lissa_compra
from config import config
# Crear el server Flask
app = Flask(__name__)

# Clave que utilizaremos para encriptar los datos
app.secret_key = "flask_session_key_inventada"

# Obtener la path de ejecución actual del script
script_path = os.path.dirname(os.path.realpath(__file__))

# Obtener los parámetros del archivo de configuración
config_path_name = os.path.join(script_path, 'config.ini')
db_config = config('db', config_path_name)
server_config = config('server', config_path_name)

# Indicamos al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_config['database']}"

#Inicializar db
tienda_lissa_venta.db.init_app(app)
tienda_lissa_compra.db.init_app(app)

# bordo #B81B43;
# blanco #FFE7ED;
# lila #DA2FB3;

@app.route("/")
def ini():
    try:

        if os.path.isfile(db_config['database']) == False:
            # Sino existe la base de datos la creo
            tienda_lissa_venta.create_schema()
            tienda_lissa_compra.create_schema()
        # Obtengo el nombre que se ingresa en el input del index
        # Transformo en lower para evitar problemas de búsqueda
        # También se guardan los nombres en lower en la db.
        #name = request.form.get("person").lower()
        #records = tienda_lissa_venta.resumen_persona(name)
        return redirect(url_for('index'))
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route("/index")
def index():
    try:

        # Obtengo el nombre que se ingresa en el input del index
        # Transformo en lower para evitar problemas de búsqueda
        # También se guardan los nombres en lower en la db.
        name = str(request.args.get("person")).lower()
        if name == None:
            return render_template("index.html")
        else:
            records = tienda_lissa_venta.resumen_persona(name)
            return render_template("index.html", records=records)
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route("/venta", methods=["GET","POST"])
def venta():

    if request.method == "GET":
        try:
            return render_template("venta.html")
        except:
            return jsonify({'trace': traceback.format_exc()})

    if request.method == "POST":

        try:
            # Obtener los datos del registro e insertarlos en la db
            name = str(request.form.get('name')).lower()

            for row in list(range(8)):
                count = request.form.get(f'count{row}')
                description = str(request.form.get(f'description{row}'))
                price = request.form.get(f'price{row}')
                date = datetime.now().date()
                # Validación de datos
                if name != None and name.isdigit() == False:
                    if (count.isdigit() == True) and (description != None) and (price.isdigit() == True):
                        tienda_lissa_venta.insert(date,name,count,description,price)
                        
            return render_template("venta.html") 
        except:
            return jsonify({'trace': traceback.format_exc()})

@app.route("/reset")
def reset():
    try:
        # Borrar y crear la base de datos
        tienda_lissa_venta.create_schema()
        tienda_lissa_compra.create_schema()
        result = "<h3>Base de datos re-generada!</h3>"
        return (result)
    except:
        return jsonify({'trace': traceback.format_exc()})

if __name__ == "__main__":
    print("Servidor funcionando!")

    app.run(host=server_config['host'],
            port=server_config['port'],
            debug=False)