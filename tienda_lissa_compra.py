#!/usr/bin/env python
'''
DB de Tienda Lissa
---------------------------
Autor: Arrascaeta Nahuel
Version: 1.0

Descripcion:
Programa creado para administrar la base de datos de compras de Tienda Lissa
'''
__author__ = "Arrascaeta Nahuel"
__email__ = "nahuelarrascaeta22@gmail.com"
__version__ = "1.0"

#Librerías
from datetime import datetime
import numpy as np
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class tienda_lissa_compra(db.Model):
    #__tablename__ = "compra"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    name = db.Column(db.String)
    count = db.Column(db.Integer)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    total = db.Column(db.Integer)
    # Integrar el fiado al final
    # pay = db.Column(db.Integer)
    # pay para saber si hay fiados

# Crear esquema
def create_schema():
    # Borrar todos las tablas existentes en la base de datos
    # Esta linea puede comentarse sino se eliminar los datos

    db.drop_all()
    # Crear las tablas
    db.create_all()

# Insertar registro
def insert(name:str, count, description:str, price):
    # Crear un nuevo registro de venta

    # Fecha actual de la creación del registro
    date = datetime.now().date()
    # el total equivale a la cantidad de prendas multiplicado por el precio
    total = int(count) * int(price)
    record_venta = tienda_lissa_compra(date=date, name=name, count=count, description=description, price=price, total=total)

    # Agregar la persona a la DB
    db.session.add(record_venta)
    db.session.commit()

# Obtener el $total de compras
def get_total():

    query_price = db.session.query(tienda_lissa_compra).filter(tienda_lissa_compra.total)
    get_query = query_price.all()

    # Sumar los totales para obtener el total de precios en general
    get_total_price = [x.total for x in get_query]
    total = np.sum(get_total_price)
    return total

# Obtener las compras realizadas
def resumen_persona(proveedor:str, limit, offset):

    json_list = []
    query_name = db.session.query(tienda_lissa_compra).filter(tienda_lissa_compra.name == proveedor)
    records_name = query_name.limit(limit).offset(offset).all()
    
    # De los registros de la persona mencionada, obtener los datos:
    for x in records_name:
        record_dict = {"id":x.id,"date":x.date, "name":x.name, "count":x.count, "description":x.description, "price":x.price, "total":x.total}
        json_list.append(record_dict)

    return json_list

# Obtener todos los registros
def db_all(limit:int, offset:int):

    query = db.session.query(tienda_lissa_compra)
    query = query.limit(limit).offset(offset).all()

    json_list = []
    # Obtener todos los registros y guardarlos en una lista:
    for x in query:
        record_dict = {"id":x.id,"date":x.date, "name":x.name, "count":x.count, "description":x.description, "price":x.price, "total":x.total}
        json_list.append(record_dict)
    
    return json_list

# Obtener registros del mes indicado
def db_month(month:str):

    query = db.session.query(tienda_lissa_compra)
    dates = query.all()

    json_list = []
    for x in dates:
        
        # Acá indico si el mes ingresado(month) es igual al mes de la fecha obtenida
        if str(x.date)[5:7] == month:
            dict_ = {"date":x.date,"id":x.id,"name":x.name,"count":x.count,"description":x.description,"price":x.price,"total":x.total}
            json_list.append(dict_)
    return json_list