# 4. Elabore un programa que permite registrar la información de los empleados
# De una compañía y le permita calcular el valor a pagar por concepto de nomina a
# Cada empleado. La información que se tiene por cada empleado es la siguiente (55ptos):

# id
# nombre
# cargo (Almacenista, Jefe IT, Administrador, Mensajero, Genrente)
# salario

# Para calcular el valor a pagar por cada empleado se debe tener en cuenta la
# Siguiente información:
# diasTrabajados
# horasExtras
# valorDia

# descuentoxCafeteria
# cuotaPrestamo

# El valor de la hora extra es de 5500 pesos. La información de la colilla de pago
# Se debe almacenar en caso de una solicitud de revisión por parte de algún
# Empleado que no este conforme con el pago la información que debe guardar
# La colilla de pago es la siguiente:

# mesPagado
# fechaPago(dd/mm/yyyy)
# sueldoBase
# valorTotalHrasExtras
# cuotaPrestamo
# descuentoxCafeteria
# totalAPagar

# La información se debe guardar en un archivo JSON.
# El gerente desea obtener la siguiente información:
# 1. Total pagado por concepto de nomina
# 2. Consultar la colilla de pago de un determinado empleado.



import os
import modulos.corefiles as core

ruta=ruta="CuartoEjercicio/data/Empleados.json"
Empleados={}

core.Checkfile("Empleados.json",Empleados)
core.ReadFile("Empleados.json")

titulo="""
+++++++++++++++++++++++++
+ REGISTRO DE EMPLEADOS +
+++++++++++++++++++++++++
"""
print(titulo)

id=input('Ingrese el ID del empleado')
nombre=input('Ingrese el nombre del empleado')
cargo=input('Ingrese el cargo del empleado')
salario=input('Ingrese el salario del empleado')



mesPagado=input('Ingrese  del empleado')
fechaPago=input('Ingrese  del empleado')
sueldoBase=input('Ingrese  del empleado')
valorTotalHrasExtras=input('Ingrese  del empleado')
cuotaPrestamo=input('Ingrese  del empleado')
descuentoxCafeteria=input('Ingrese  del empleado')
totalAPagar=input('Ingrese  del empleado')

Empleado={
    'id':id,
    'nombre':nombre,
    'cargo':cargo, 
    'salario':salario,
    'colilla':{
        'mesPagado':mesPagado,
        'fechaPago':fechaPago,
        'sueldoBase':sueldoBase,
        'valorTotalHrasExtras':valorTotalHrasExtras,
        'cuotaPrestamo':cuotaPrestamo,
        'descuentoxCafeteria':descuentoxCafeteria,
        'totalAPagar':totalAPagar
    }
}





Empleado.update({id:Empleado})
core.UpdateFile(Empleados)
print (Empleados)