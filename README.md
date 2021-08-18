# Tienda Lissa DB

**Proyecto para aprobar conocimientos brindados por inoveARG**
![inove_logo](https://inove.com.ar/wp-content/uploads/2020/03/cropped-3-1.png)

Sitio web para administrar las compras y ventas de una tienda de ropa y calzados.
El propósito de este proyecto es digitalizar los controles diarios de compra/venta de tienda Lissa

## Características:

- Facturero de compra/venta
- Buscador de registros mediante el nombre
- Buscador de registros mediante el mes
- Resumen diario de ventas
- Resumen de fiados
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
            - fiado.js
    - templates
        - compra
            - compra.html
            - buscar_compra_por_mes.html
            - buscar_por_proveedor.html
        - venta
            - venta.html
            - buscar_venta_por_mes.html
            - resumen_venta_diario.html
        - fiado.html
        - index.html
    app.py
    config.ini
    config.py
    tienda_lissa_compra.py
    tienda_lissa_venta.py
    Diagrama_tienda_lissa_db.drawio

## Tecnologías que se usaron:

- **Python 3.8.3**
- **Flask 2.0.1**
- **ORM sqlalchemy**
- **HTML, CSS y JS**

## Guía de uso:

Consta de 10 endpoints
- /inicio
- /venta
    - /buscar_venta_por_mes
    - /resumen_venta_diario
- /compra
    - /buscar_compra_por_mes
    - /buscar_por_proveedor
- /fiado
- /resumen
- /reset

### Inicio

En este endpoint podemos buscar por nombre a los registros de venta de la db

**El registro impreso cuenta con 7 columnas**
- Fecha
- ID
- Nombre
- Cantidad
- Descripción
- Precio unitario
- Precio total
- Fiado

__Palabras clave para las busquedas__
- /all: Muestra todos los registros de ventas de la db
- name: Ingresar nombre de alguna persona registrada
<!-- Mostrar imagen de la interfaz de inicio -->
![inicio_tienda_lissa_db](https://github.com/NahuelA/Proyecto_programador_py_inove/blob/main/main/static/media/inicio.png)

### Venta

Muestra un formulario para registrar hasta 8 ventas

**Las entradas del formulario son las siguientes**
- Nombre
- Cantidad
- Descripción
- Precio unitario

__Los nombres se guardan en lower_case y en el buscador de registros de inicio también se pasa el nombre ingresado a lower_case__
<!-- Mostrar imagen de la interfaz de inicio -->

### Compra