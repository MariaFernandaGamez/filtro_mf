import os

def ValINT():
    try:
        x=int(input(''))
        return x
    except ValueError:
        print('Dato invalido, intentelo de nuevo')
        return ValINT()
