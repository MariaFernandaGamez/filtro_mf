# 1. Elabore un programa en Python que permita convertir de pesos a dólares, de
# pesos a euros, de euros a pesos, de pesos a yenes. (10 ptos)
# 1 yen = 26.30 pesos
# 1 dólar = 3944 pesos
# 1 euro = 4279 pesos


import os 
from tabulate import tabulate
import validaciones as val


titulo="""
    +++++++++++++++++++++++++++++++++++
    +        CONVERTIR MONEDAS        +
    +++++++++++++++++++++++++++++++++++

"""
print(titulo)

print('Ingrese una cantidad de pesos')
pesos=val.ValINT()
#=val.ValFloat()

Ayan=pesos/26.30
pesosAdolar=pesos*3944
pesosAeuro=pesos*4279
eurosApesos=pesos/4279

print('Ingrese una cantidad de euros')
euros=val.ValINT()

eurosApesos=euros*4279


print(f'${pesos} pesos equivalen a ${Ayan} yanes')
print(f'${pesos} pesos equivalen a ${pesosAdolar} dolares')
print(f'${pesos} pesos equivalen a ${pesosAeuro} euros')
print(f'${euros} euros equivalen a ${eurosApesos} pesos')

