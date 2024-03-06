# 2. Elabore un programa en Python que permita leer la información de un usuario
# Y la almacene en un diccionario. La información del usuario es la siguiente(15 ptos):
# id
# nombres
# apellidos
# ubicación
# dirección
# ciudad
# longitud
# latitud
# email
# edad
# ocupación

titulo="""
    ++++++++++++++++++++++++
    + REGISTRO DE USUARIOS +
    ++++++++++++++++++++++++
"""
print(titulo)

usuario={}


id=(input('Ingrese id del usuario\n'))
nombres=str(input('Ingrese nombres del usuario\n'))
apellidos=str(input('Ingrese apellidos del usuario\n'))
dirección=int(input('Ingrese dirección del usuario\n'))
ciudad=str(input('Ingrese ciudad del usuario\n'))
longitud=int(input('Ingrese longitud del usuario\n'))
latitud=int(input('Ingrese latitud del usuario\n'))
email=input('Ingrese email del usuario\n')
edad=int(input('Ingrese edad del usuario\n'))
ocupación=str(input('Ingrese ocupación del usuario\n'))

Usuario={
    'id':    id,
    'nombres':    nombres,
    'apellidos':    apellidos,
    'ubicacion':{
        'dirección':    dirección,
        'ciudad':    ciudad,
        'longitud':    longitud,
        'latitud':    latitud,
        'email':    email,
        'edad':    edad,
        'ocupación':    ocupación,
    }
    }

usuario.update({id:Usuario})

print(usuario)