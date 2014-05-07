from ctypes import *
from pyswip.prolog import Prolog


def agregarPlatillo(restaurante,platillo,tipo,pais,ingredientes):
    plat = platillo.replace(" ","_")
    ingred = ingredientes.replace(" ","")
    p = open("base.pl","a")
    p.write("platillos("+restaurante+","+plat+","+pais+","+ingred+").\n")
    p.close()
    texto = open("info.txt","a")
    lista1 = ingred.replace("[","")
    lista2 = lista1.replace("]","")
    listaIngredientes = lista2.replace(","," ")
    texto.write("platillos "+restaurante+" "+plat+" "+tipo+" "+pais+" "+listaIngredientes+" \n")
    texto.close()
    
def agregarRestaurante(nombre,comida,ubicacion,telefono):
    p = open("base.pl","a")
    p.write("restaurantes("+nombre+","+comida+","+ubicacion+","+telefono+").\n")
    p.close()
    texto = open("info.txt","a")
    texto.write("restaurantes "+nombre+" "+comida+" "+ubicacion+" "+telefono+" \n")
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
    for datos in p.query("platillos("+restaurante+",Platillo,Tipo,Ingredientes)"):
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
    linea=texto.readline()
    while linea!="":
        datoLinea = linea.split(" ",1)
        if(datoLinea[0]=="restaurante"):
            restaurante = linea.split(" ",5)
            nombre = " Restaurante: "+ restaurante[1]
            datosRestaurantes.append(nombre)
            demas = "Tipo de comida: "+ restaurante[2]+" Ubicacion: "+ restaurante[3]+" Telefono "+ restaurante[4]
            datosRestaurantes.append(demas)
            espacio = " "
            datosRestaurantes.append(espacio)
        linea=texto.readline()
    texto.close()
    return datosRestaurantes

def listaRestaurantes():
    listarestaurantes = []
    texto = open("info.txt","r")
    linea=texto.readline()
    while linea!="":
        datoLinea = linea.split(" ",1)
        if(datoLinea[0]=="restaurante"):
            restaurante = linea.split(" ",5)
            nombre = restaurante[1]
            listarestaurantes.append(nombre)
        linea=texto.readline()
    texto.close()
    return listarestaurantes
