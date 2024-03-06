# 3. Elabore un programa en Python que permita registrar los productos de una
# Tienda de viveres. La información se debe almacenar en un archivo JSON. La
# Información de los productos es la siguiente (20ptos):

# id
# nombre
# valorUnitario
# stockmin
# stockmax
# valorUnitario

import modulos.corefiles as core

Productos={}
core.Checkfile("Tienda.json",Productos)
core.ReadFile("Tienda.json")
ruta="TercerEjercicio/data/Tienda.json"

titulo="""
++++++++++++++++++++++++++
+  REGISTRO DE PRODUCTOS +
++++++++++++++++++++++++++
"""
print(titulo)
Cierre=True
while Cierre:
    id=float(input('Ingrese el id del producto'))
    nombre=input('Ingrese el nombre del producto')
    valorUnitario=float(input('Ingrese el valor unitario del producto'))
    stockmin=float(input('Ingrese el stock minimo del producto'))
    stockmax=float(input('Ingrese el stock maximo del producto'))
    valorVenta=float(input('Ingrese el valor de venta del producto'))

    producto={
        'id':id,
        'nombre':nombre,
        'valorUnitario':valorUnitario,
        'stockmin':stockmin,
        'stockmax':stockmax,
        'valorVenta':valorVenta
    }
    Productos.update({id:producto})
    core.UpdateFile(ruta,Productos)

    Cierre=bool(input('¿Desea agregar mas productos? TECLA(si) ENTER(no)'))
print(Productos)