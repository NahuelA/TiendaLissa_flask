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
import os
#Matplotlib para realizar un balance general de ventas y compras
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#Flask
from flask import Flask, request, jsonify, render_template, Response, redirect, url_for
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
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///../db/{db_config['database']}"

#Inicializar db
tienda_lissa_venta.db.init_app(app)
tienda_lissa_compra.db.init_app(app)


# FUNCIONES PARA EL PROGRAMA
# Transformar figura a imagen
def plot_to_canvas(fig):
    # Convertir ese grafico en una imagen para enviar por HTTP
    # y mostrar en el HTML
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return output
# Realizado


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
        return redirect(url_for('index'))
    except:
        return jsonify({'trace': traceback.format_exc()})
# Realizado


# Nota: El endpoint tiene que ser el mismo nombre que la función decorada
# INDEX
@app.route("/index")
def index():
    try:

        # Obtengo el nombre que se ingresa en el input del index
        # Transformo en lower para evitar problemas de búsqueda
        # También se guardan los nombres en lower en la db.
        name = str(request.args.get("person")).lower()
        limit = request.args.get("limit")
        offset = request.args.get("offset")
        
        if name == None:
            return render_template("index.html")
        elif name == "/all":
            records = tienda_lissa_venta.db_all(limit, offset)
            return render_template("index.html", records=records)
        else:
            records = tienda_lissa_venta.resumen_persona(name, limit, offset)
            return render_template("index.html", records=records)
    except:
        return jsonify({'trace': traceback.format_exc()})
# Realizado


# VENTA
@app.route("/venta", methods=["GET","POST"])
def venta():

    if request.method == "GET":
        try:
            return render_template("venta/venta.html")
        except:
            return jsonify({'trace': traceback.format_exc()})

    if request.method == "POST":

        try:
            # Obtener los datos del registro e insertarlos en la db
            name = str(request.form.get('name')).lower()

            # Bucle for para iterar todos los campos del formulario de venta
            for row in list(range(8)):
                count = request.form.get(f'count{row}')
                description = str(request.form.get(f'description{row}'))
                price = request.form.get(f'price{row}')
                
                # Validación de datos
                if name != None and name.isdigit() == False:
                    if (count.isdigit() == True) and (description != None) and (price.isdigit() == True):
                        tienda_lissa_venta.insert(name,count,description,price)
            return render_template("venta/venta.html")
        except:
            return jsonify({'trace': traceback.format_exc()})
# Realizado


# BUSCAR VENTA POR MES
@app.route("/buscar_venta_por_mes", methods=["GET","POST"])
def buscar_venta_por_mes():

    if request.method == "GET":
        try:
            return render_template("venta/buscar_venta_por_mes.html")
        except:
            return jsonify({'trace': traceback.format_exc()})

    if request.method == "POST":
        try:
            month = str(request.form.get("date"))
            # Validación
            if month.isdigit() == False:
                return render_template("venta/buscar_venta_por_mes.html")
            elif month.isdigit() == True:
                records = tienda_lissa_venta.db_month(month)
                return render_template("venta/buscar_venta_por_mes.html",records=records)
        except:
            return jsonify({'trace': traceback.format_exc()})
# Realizado


# COMPRA
@app.route("/compra", methods=["GET","POST"])
def compra():

    if request.method == "GET":
        try:
            return render_template("compra/compra.html")
        except:
            return jsonify({'trace': traceback.format_exc()})

    if request.method == "POST":

        try:
            # Obtener los datos del registro e insertarlos en la db
            name = str(request.form.get('name')).lower()
            # Bucle for para iterar todos los campos del formulario de venta
            for row in list(range(8)):
                count = request.form.get(f'count{row}')
                description = str(request.form.get(f'description{row}'))
                price = request.form.get(f'price{row}')
                
                # Validación de datos
                if name != None and name.isdigit() == False:
                    if (count.isdigit() == True) and (description != None) and (price.isdigit() == True):
                        tienda_lissa_compra.insert(name,count,description,price)            
            return render_template("compra/compra.html")
        except:
            return jsonify({'trace': traceback.format_exc()})
# Realizado


# BUSCAR COMPRA POR MES
@app.route("/buscar_compra_por_mes", methods=["GET","POST"])
def buscar_compra_por_mes():

    if request.method == "GET":
        try:
            return render_template("compra/buscar_compra_por_mes.html")
        except:
            return jsonify({'trace': traceback.format_exc()})

    if request.method == "POST":
        try:
            month = str(request.form.get("date"))
            # Validación
            if month.isdigit() == False:
                return render_template("compra/buscar_compra_por_mes.html")
            elif month.isdigit() == True:
                records = tienda_lissa_compra.db_month(month)
                return render_template("compra/buscar_compra_por_mes.html",records=records)
        except:
            return jsonify({'trace': traceback.format_exc()})
# Realizado


# BUSCAR COMPRA POR PROVEEDOR
@app.route("/buscar_por_proveedor")
def buscar_por_proveedor():
    try:

        # Obtengo el nombre que se ingresa en el input del template
        # Transformo en lower para evitar problemas de búsqueda
        # También se guardan los nombres en lower en la db.
        proveedor = str(request.args.get("proveedor")).lower()
        limit = request.args.get("limit")
        offset = request.args.get("offset")
        
        if proveedor == None:
            return render_template("compra/buscar_por_proveedor.html")
        elif proveedor == "/all":
            records = tienda_lissa_compra.db_all(limit, offset)
            return render_template("compra/buscar_por_proveedor.html", records=records)
        else:
            records = tienda_lissa_compra.resumen_persona(proveedor, limit, offset)
            return render_template("compra/buscar_por_proveedor.html", records=records)
    except:
        return jsonify({'trace': traceback.format_exc()})
# Realizado


# RESUMEN
@app.route("/resumen")
def resumen():
    try:
        venta  = tienda_lissa_venta.get_total()
        compra = tienda_lissa_compra.get_total()
        # La figura muestra una suba si la compra de mercadería está acorde con las ventas
        # Si baja es porque se compra más de lo que se vende
        fig,ax = plt.subplots()
        ax.plot(compra, venta, label = "Compra = Costo | Venta = Costo + Ganancia")
        plt.legend()
        # Retorna el valor de la figura en bytes
        output = plot_to_canvas(fig)
        plt.close(fig)# Cerramos la img para que no consuma memoria
        return Response(output.getvalue(),mimetype='image/png')
    except:
        return jsonify({'trace': traceback.format_exc()})
# Realizado


# RESET
@app.route("/reset")
def reset():
    try:
        # Borra la db y la vuelve a crear en la misma ubicación 
        # app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///../db/{db_config['database']}"
        if os.path.isfile(db_config['database']) == True:
            # Borrar y crear base de datos
            tienda_lissa_venta.create_schema()
            tienda_lissa_compra.create_schema()
        result = "<h3>Base de datos re-generada!</h3>"
        return (result)
    except:
        return jsonify({'trace': traceback.format_exc()})
# Realizado
# Nota: Más adelante se puede crear un template para el endpoint /reset

if __name__ == "__main__":
    app.run(host=server_config['host'],
            port=server_config['port'],
            debug=False)