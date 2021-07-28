# Tienda Lissa DB

**Proyecto para aprobar conocimientos brindados por inoveARG**
![inove_logo](https://inove.com.ar/wp-content/uploads/2020/03/cropped-3-1.png)

Sitio web para administrar las compras y ventas de una tienda de ropa y calzados.
El propósito de este proyecto es Digitalizar los controles diarios de compra/venta de la tienda

## Características:

- Facturero de compra/venta
- Buscador de registros mediante el nombre
- Gráfico que muestra un balance entre compra/venta
- Reset de db

## Pre-requisitos:

- Tener instalado **Python 3.8.3**
- Tener instalado **Flask**
- Tener instalado **numpy**

## Esquema del proyecto:

- db
    - schema.sql
    - tienda_lissa.db
- main
    - static
        - media
            - search-solid.svg
        - src
            - main.css
            - main.js
    - templates
        - compra
            - compra.html
            - buscar_compra_por_mes
            - buscar_por_proveedor
        - venta
            - venta.html
            - buscar_venta_por_mes
        - fiado.html
        - index.html
    app.py
    config.ini
    config.py
    tienda_lissa_compra.py
    tienda_lissa_venta.py

## Herramientas que se usaron:

- **Python 3.8.3**
- **Flask 2.0.1**
- **ORM sqlalchemy**
- **HTML y CSS**

## Guía de uso:

El sitio consta de 9 endpoints

- (1) inicio
- (2) venta
    - (3) buscar por mes
- (4) compra
    - (5) buscar por mes
    - (6) buscar por proveedor
- (7) fiado
- (8) resumen
- (9) reset

## Inicio

En este endpoint podemos buscar por nombre a los registros de venta de la db

**El registro impreso cuenta con 7 columnas**
- Fecha
- ID
- Nombre
- Cantidad
- Descripción
- Precio unitario
- Precio total
__La columna fecha, id y total se generan dinámicamente__

__Palabras clave para las busquedas__
- /all: Muestra todos los registros de la db
- name: Ingresar nombre de alguna persona registrada
<!-- Mostrar imagen de la interfaz de inicio -->

## Venta

Muestra un formulario para registrar hasta 8 ventas

**Las entradas del formulario son las siguientes**
- Nombre
- Cantidad
- Descripción
- Precio unitario

__Los nombres se guardan en lower_case y en el buscador de registros de inicio también se pasa el nombre ingresado a lower_case__
<!-- Mostrar imagen de la interfaz de inicio -->

## Compra