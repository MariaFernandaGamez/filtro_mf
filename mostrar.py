def Search():
    titulo=[['|                   BUSCAR PERSONAL                |']]
    print(val.tabulate(titulo,tablefmt='rounded_grid'))
    llave="personal"
    with open(ruta, "r") as read:
        dictCampus = json.loads(read.read())
    listPersonal=[]
    if len(dictCampus["personal"])>0:
        for i in dictCampus["personal"]:
            persona=[i,dictCampus["personal"][i]["nombre"]]
            listPersonal.append(persona)
        print(val.tabulate(listPersonal,tablefmt="heavy_grid"))
    print('Ingrese el ID del personal')
    Id=val.ValidarKey(dictCampus,llave)
    persona=dictCampus['personal'][str(Id)]
    ListPersonal=[[persona["id"],persona["nombre"],persona["oficina"]]]
    print(val.tabulate(ListPersonal,headers=["ID del personal","nombre","Telefono de oficina"]))
    x=str(input('Digite cualquier letra para continuar'))

def ListaActBaja():
    val.os.system('clear')
    with open(ruta, "r") as read:
        dictCampus = json.loads(read.read())
    listaActivos=[]
    for i in dictCampus['activos']:
        if dictCampus['activos'][i]["Estado"]==2:
            activo=[i,dictCampus['activos'][i]["nombre"],dictCampus['activos'][i]["Marca"],dictCampus['activos'][i]["Tipo"],dictCampus['activos'][i]["Estado"]]
            listaActivos.append(activo)
    if (len(listaActivos))==0:
        print('No hay activos dados de baja')
    else: 
        pass
        print(val.tabulate(listaActivos,headers=["CODIGO","NOMBRE","MARCA","TIPO","ESTADO"],tablefmt="rounded_grid"))
    x=(input('Digite cualquier tecla para salir: \n'))