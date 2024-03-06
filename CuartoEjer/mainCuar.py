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

#valordia=sALARIO/30

import os

import modulos.corefiles as core

ruta="Empleados.json"
Empleados={}

core.Checkfile("Empleados.json",Empleados)
Empleados=core.ReadFile("Empleados.json")

titulo="""
+++++++++++++++++++++++++
+ REGISTRO DE EMPLEADOS +
+++++++++++++++++++++++++
"""
print(titulo)

menu="""
    1.Agregar empleados
    2.Leer Colillas
"""
print(menu)
op=int(input(('Seleccione la opcion')))
if op==1:
    id=input('Ingrese el ID del empleado')
    nombre=input('Ingrese el nombre del empleado')
    cargo=input('Ingrese el cargo del empleado')

    salario=float(input('Ingrese el salario del empleado'))
    diasTrabajados=float(input('Ingrese los dias trabajados por el empleado'))
    horasExtras=float(input('Ingrese las horas extras trabajadas por el empleado'))
    descuentoxCafeteria=float(input('Ingrese el valor del descuento por cafeteria del empleado'))
    cuotaPrestamo=float(input('Ingrese el valor de la cuota del prestamo del empleado'))

    ValorDia=salario/30
    valorTotalHrasExtras=horasExtras*5500
    ValorMes=ValorDia*diasTrabajados
    Descontar=descuentoxCafeteria+cuotaPrestamo
    ValorPagar=ValorMes+valorTotalHrasExtras
    totalAPagar=ValorPagar-Descontar

    mesPagado=input('Ingrese el mes que le pagara al empleado')
    fechaPago=input('Ingrese la fecha en la que se efectua el pago al empleado')
    print(f'El valor a pagar por {horasExtras} horas extras trabajadas es de {valorTotalHrasExtras} ')
    print(f'El total a pagar al empleado es: ${totalAPagar}')

    Empleado={
        'id':id,
        'nombre':nombre,
        'cargo':cargo, 
        'salario':salario,
        'colilla':{
            'mesPagado':mesPagado,
            'fechaPago':fechaPago,
            'valorTotalHrasExtras':valorTotalHrasExtras,
            'cuotaPrestamo':cuotaPrestamo,
            'descuentoxCafeteria':descuentoxCafeteria,
            'totalAPagar':totalAPagar
        }
    }
    Empleados.update({id:Empleado})
    core.UpdateFile(ruta,Empleados)
    print (Empleados)
elif op==2:
    def ValidarKey(Empleados,id):
        try:
            x=str(input(''))
            Empleados[x]
            return x
        except KeyError:
            print('Elemento no existente')
            return ValidarKey(Empleados,id)

    print('Ingrese el ID del empleado')
    id=ValidarKey(Empleados,"Empleado")
    Empleado=Empleados[id]['colilla']
    print(Empleado)