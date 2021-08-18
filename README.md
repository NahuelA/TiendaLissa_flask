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

Muestra un formulario para registrar hasta 8 ventas por vez

**Las entradas del formulario son las siguientes**
- Nombre
- Cantidad
- Descripción del producto
- Precio unitario
- Fiado

<!-- Mostrar imagen de la interfaz de venta -->
![venta_tienda_lissa_db](https://github.com/NahuelA/Proyecto_programador_py_inove/blob/main/main/static/media/venta.png)

### Buscar venta por mes

Al ingresar el mes deseado se imprimen las ventas registradas en esa fecha

![buscar_venta_por_mes_tienda_lissa_db](https://github.com/NahuelA/Proyecto_programador_py_inove/blob/main/main/static/media/buscar_por_mes.png)

### Resumen venta diario

Muestra las ventas registradas durante el día

![buscar_venta_por_mes_tienda_lissa_db](https://github.com/NahuelA/Proyecto_programador_py_inove/blob/main/main/static/media/resumen_diario.png)

### Compra

Muestra un formulario para registrar hasta 8 compras por vez

**Las entradas del formulario son las siguientes**
- Nombre del proveedor
- Cantidad
- Descripción del producto
- Precio unitario

![compra_tienda_lissa_db](https://github.com/NahuelA/Proyecto_programador_py_inove/blob/main/main/static/media/compra.png)

### Buscar compra por mes

Al ingresar el mes deseado se imprimen las compras registradas en esa fecha

![buscar_compra_por_mes_tienda_lissa_db](https://github.com/NahuelA/Proyecto_programador_py_inove/blob/main/main/static/media/buscar_compra_por_mes.png)

### Buscar por proveedor

En este endpoint podemos buscar por nombre a los registros de compra de la db

![buscar_por_proveedor_tienda_lissa_db](https://github.com/NahuelA/Proyecto_programador_py_inove/blob/main/main/static/media/buscar_compra.png)

### Fiado

Aquí aparecerán todos los registros que fueron guardados con el checkbox de fiado marcado

**Tiene la opción de pagado al marcar el checkbox**

![fiado_tienda_lissa_db](https://github.com/NahuelA/Proyecto_programador_py_inove/blob/main/main/static/media/fiado.png)

### Resumen

Aquí aparece el resumen general de compra/venta

![resumen_tienda_lissa_db](https://github.com/NahuelA/Proyecto_programador_py_inove/blob/main/main/static/media/grafico.png)

## Actualizaciones

Proximamente...

## Versión

**1.0**

## Autor

Nahuel_A
**Correo:** nahuelarrascaeta22@gmail.com