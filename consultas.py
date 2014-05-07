from ctypes import *
from pyswip.prolog import Prolog

def agregarPlatillo(restaurante,platillo,tipo,pais,ingredientes):
    plat = (platillo.replace(" ","_")).lower()
    ingred = (ingredientes.replace(" ","")).lower()
    p = open("base.pl","a")
    p.write("platillos("+restaurante+","+plat+","+tipo+","+pais+","+ingred+").\n")
    p.close()
    texto = open("info.txt","a")
    lista1 = ingred.replace("[","")
    lista2 = lista1.replace("]","")
    listaIngredientes = lista2.replace(","," ")
    texto.write("platillos "+restaurante+" "+plat+" "+tipo+" "+pais+" "+listaIngredientes+" \n")
    texto.close()
    
def agregarRestaurante(nombre,comida,ubicacion,telefono):
    nom = (nombre.replace(" ","_")).lower()
    comid = (comida.replace(" ","_")).lower()
    ubic = (ubicacion.replace(" ","_")).lower()
    telef = (telefono.replace(" ","-")).lower()
    p = open("base.pl","a")
    p.write("restaurantes("+nom+","+comid+","+ubic+","+telef+").\n")
    p.close()
    texto = open("info.txt","a")
    texto.write("restaurantes "+nom+" "+comid+" "+ubic+" "+telef+" \n")
    texto.close()

def verRestaurantes():
    p=Prolog()
    p.consult('base.pl')
    restaurantes = [] 
    for datos in p.query("restaurantes(Nombre,Comida,Ubicacion,Telefono)"):
        restaurantes.append(datos["Nombre"])
        restaurantes.append(datos["Comida"])
        restaurantes.append(datos["Ubicacion"])
        restaurantes.append(datos["Telefono"])
    i = 0
    while (len(restaurantes) != i):
        print restaurantes[i]
        i = i + 1

def platilloXrestaurante(restaurante):
    p=Prolog()
    p.consult('base.pl')
    platillo = [] 
    for datos in p.query("platillos("+restaurante+",Platillo,Pais,Ingredientes)"):
        platillo.append(datos["Platillo"])
        platillo.append(datos["Tipo"])
        platillo.append(datos["Ingredientes"])
    i = 0
    deter = 1
    while (len(platillo) != i):
        if(deter==3):
            ingredientes = platillo[i]
            indice = 0
            while (len(ingredientes)!=indice):
                print(platillo[i][indice])
                indice = indice + 1
            deter = 0
        else:
            print platillo[i]
        i = i + 1
        deter = deter + 1

def obtenerRestaurantes():
    datosRestaurantes = []
    texto = open("info.txt","r")
    for dato in texto:
        datoLinea = dato.split(" ",1)
        if(datoLinea[0]=="restaurantes"):
            restaurante = dato.split(" ",5)
            nombre = " Restaurante: "+ restaurante[1]
            datosRestaurantes.append(nombre)
            demas = "Tipo de comida: "+ restaurante[2]+" Ubicacion: "+ restaurante[3]+" Telefono "+ restaurante[4]
            datosRestaurantes.append(demas)
            espacio = " "
            datosRestaurantes.append(espacio)
    texto.close()
    return datosRestaurantes

def listaRestaurantes():
    listarestaurantes = []
    texto = open("info.txt","r")
    linea=texto.readline()
    while linea!="":
        datoLinea = linea.split(" ",1)
        if(datoLinea[0]=="restaurantes"):
            restaurante = linea.split(" ",5)
            nombre = restaurante[1]
            listarestaurantes.append(nombre)
        linea=texto.readline()
    texto.close()
    return listarestaurantes

def obtenerPlatilloRest(restaurante):
    datosPlatillos = []
    texto = open("info.txt","r")
    for dato in texto:
        datoLinea = dato.split(" ",1)
        if(datoLinea[0]=="platillos"):
            platillo = dato.split(" ",5)
            if(platillo[1]==restaurante):
                nombre ="Platillo: "+platillo[2]
                datosPlatillos.append(nombre)
                ingredientes = "Ingredientes: "+platillo[5]
                datosPlatillos.append(ingredientes)
                espacio = " "
                datosPlatillos.append(espacio)
    texto.close()
    return datosPlatillos

def busquedaRestaurante(tipo,valor):
    p=Prolog()
    p.consult('base.pl')
    resultado = []
    if (tipo=="TipoComida"):
        for datos in p.query("restaurantes(Nombre,"+valor+",_,_)"):
            resultado.append(datos["Nombre"])
        i = 0
        while (len(resultado) != i):
            print resultado[i]
            i = i + 1
    elif(tipo=="Platilloxpais"):
        for datos in p.query("platillos(Nombre,_,_,"+valor+",_)"):
            resultado.append(datos["Nombre"])
        i = 0
        while (len(resultado) != i):
            print resultado[i]
            i = i + 1
