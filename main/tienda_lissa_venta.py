#!/usr/bin/env python
'''
DB de Tienda Lissa
---------------------------
Autor: Arrascaeta Nahuel
Version: 1.0

Descripcion:
Programa creado para administrar la base de datos de ventas de Tienda Lissa
'''
__author__ = "Arrascaeta Nahuel"
__email__ = "nahuelarrascaeta22@gmail.com"
__version__ = "1.0"

#Librerías
from datetime import date, datetime
from re import MULTILINE
import numpy as np
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import query_expression
db = SQLAlchemy()


class tienda_lissa_venta(db.Model):
    __tablename__ = "venta"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    name = db.Column(db.String)
    count = db.Column(db.Integer)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    total = db.Column(db.Integer)
    # Integrar el fiado al final
    pay = db.Column(db.String)
    # pay para saber si hay fiados


def create_schema():
    # Borrar todos las tablas existentes en la base de datos
    # Esta linea puede comentarse sino se eliminar los datos
    db.drop_all()
    # Crear las tablas
    db.create_all()

def insert(name:str, count, description:str, price, pay:str):
    # Crear un nuevo registro de venta
    
    # Fecha actual de la creación del registro
    date = datetime.now().date()
    # el total equivale a la cantidad de prendas multiplicado por el precio
    total = int(count) * int(price)
    record_venta = tienda_lissa_venta(date=date, name=name, count=count, description=description, price=price, total=total, pay=pay)

    # Agregar la persona a la DB
    db.session.add(record_venta)
    db.session.commit()


# Obtener el total de precios
def get_total():

    query_price = db.session.query(tienda_lissa_venta).filter(tienda_lissa_venta.total)
    get_query = query_price.all()

    # Sumar los totales para obtener el total de precios en general
    get_total_price = [x.total for x in get_query]
    total = np.sum(get_total_price)
    return total


# Obtener las ventas realizadas
def resumen_persona(name:str,limit, offset):

    json_list = []
    query_name = db.session.query(tienda_lissa_venta).filter(tienda_lissa_venta.name == name)
    records_name = query_name.limit(limit).offset(offset).all()

    # De los registros de la persona mencionada, obtener los datos:
    for x in records_name:
        record_dict = {"id":x.id,"date":x.date, "name":x.name, "count":x.count, "description":x.description, "price":x.price, "total":x.total, "fiado":x.pay}
        json_list.append(record_dict)

    return json_list


# Obtener todos los registros
def db_all(limit:int, offset:int):

    query = db.session.query(tienda_lissa_venta)
    query = query.limit(limit).offset(offset).all()

    json_list = []
    # Obtener todos los registros y guardarlos en una lista:
    for x in query:
        record_dict = {"id":x.id,"date":x.date, "name":x.name, "count":x.count, "description":x.description, "price":x.price, "total":x.total, "fiado":x.pay}
        json_list.append(record_dict)
    
    return json_list


# Obtener registros del mes indicado
def db_month(month:str):

    query = db.session.query(tienda_lissa_venta)
    dates = query.all()

    json_list = []
    for x in dates:
        
        # Acá indico si el mes ingresado(month) es igual al mes de la fecha obtenida
        if str(x.date)[5:7] == month:
            dict_ = {"date":x.date,"id":x.id,"name":x.name,"count":x.count,"description":x.description,"price":x.price,"total":x.total, "fiado":x.pay}
            json_list.append(dict_)
    return json_list


# Obtener los fiados
def get_fiados():
    query = db.session.query(tienda_lissa_venta)
    dates = query.all()

    json_list = []
    for x in dates:
        if x.pay == "debe":
            # Acá indico si el mes ingresado(month) es igual al mes de la fecha obtenida
            dict_ = {"date":x.date,"id":x.id,"name":x.name,"count":x.count,"description":x.description,"price":x.price,"total":x.total, "fiado":x.pay}
            json_list.append(dict_)
    return json_list

# Borrar fiados
def paid(id,paid:str):
    
    fiados = get_fiados()
    for fiado in range(len(fiados)):
        # dict_ = {"date":fiado["date"],
        #         "id":fiado["id"],
        #         "name":fiado["name"],
        #         "count":fiado["count"],
        #         "description":fiado["description"],
        #         "price":fiado["price"],
        #         "total":fiado["total"],
        #         "fiado":fiado["fiado"]
        #         }
        if id == fiados[fiado]["id"] and paid == "pagado":
            query = db.session.query(tienda_lissa_venta).filter(tienda_lissa_venta.id == id)
            user_delete = query.first()
            # Eliminar registro de fiado porque ya está saldada su cuenta
            db.session.delete(user_delete)
            # insert(dict_["name"], dict_["count"], dict_["description"], dict_["price"], paid)
            db.session.commit()
    return None
        


# Obtener resumen de venta diario
def resumen_venta_diario():
    # Filtrar los registros de venta de hoy
    date = datetime.now().date()
    query = db.session.query(tienda_lissa_venta)
    query_all = query.all()

    json_list = []
    for sale in query_all:
        if str(sale.date)[8:10] == str(date)[8:10]:
            dict_ = {"date":sale.date,"id":sale.id,"name":sale.name,"count":sale.count,"description":sale.description,"price":sale.price,"total":sale.total, "fiado":sale.pay}
            json_list.append(dict_)
    
    return json_list
