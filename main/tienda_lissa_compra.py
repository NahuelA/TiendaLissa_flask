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
    # pay = db.Column(db.Integer)

def create_schema():
    # Borrar todos las tablas existentes en la base de datos
    # Esta linea puede comentarse sino se eliminar los datos

    db.drop_all()
    # Crear las tablas
    db.create_all()

def insert(date, name, count, descrption, price, total, pay):
    # Crear un nuevo registro de venta
    record_venta = tienda_lissa_compra(date=date, name=name, count=count, descrption=descrption, price=price)

    # Agregar la persona a la DB
    db.session.add(record_venta)
    db.session.commit()

# Obtener el limit y offset del HTTP POST
def limit_offset(limit, offset):
    pass

# Obtener el $total de compras
def get_total():

    query_price = db.session.query(tienda_lissa_compra).filter(tienda_lissa_compra.price)
    get_query = query_price.all()

    # Sumar todos los precios para obtener el total de ventas en general
    get_total_price = [x.price for x in get_query]
    total = np.sum(get_total_price)
    return total

# Obtener el resumen de compra de Tienda Lissa
def resumen_persona(proveedor):

    json_list = []
    query_name = db.session.query(tienda_lissa_compra).filter(tienda_lissa_compra.name == proveedor)
    records_name = query_name.all()

    if len(records_name) == 0:    
        return "<h1> No se encontraron registros con dicho nombre </h1>"
    
    # De los registros de la persona mencionada, obtener los datos:
    for x in records_name:
        record_dict = {"date":x.date, "name":x.name, "count":x.count, "description":x.description, "price":x.price}
        json_list.append(record_dict)

    return json_list