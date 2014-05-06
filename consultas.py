from ctypes import *
from pyswip.prolog import Prolog

def agregarPlatillo(restaurante,platillo,tipo,pais,ingredientes):
    p = open("base.pl","a")
    p.write("platillos("+restaurante+","+platillo+","+pais+","+ingredientes+").\n")
    p.close()
    
def agregarRestaurante(nombre,comida,ubicacion,telefono):
    p = open("base.pl","a")
    p.write("restaurantes("+nombre+","+comida+","+ubicacion+","+telefono+").\n")
    p.close()
    texto = open("base.pl","a")
    texto.write("restaurantes "+nombre+" "+comida+" "+ubicacion+" "+telefono+" \n")
    texto.close()

def verRestaurantes():
    p=Prolog()
    p.consult('base.pl')
    print (list(p.query("restaurantes(Nombre,Comida,Ubicacion,Telefono)")))

def obtenerRestaurantes():
    datosRestaurantes = ""
    texto = open("info.txt","r")
    linea=texto.readline()
    while linea!="":
        datoLinea = linea.split(" ",1)
        if(datoLinea[0]=="restaurante"):
            restaurante = linea.split(" ",5)
            datosRestaurantes= datosRestaurantes + " Restaurante: "+ restaurante[1]
            datosRestaurantes= datosRestaurantes + " Tipo de comida "+ restaurante[2]
            datosRestaurantes= datosRestaurantes + " Ubicacion "+ restaurante[3]
            datosRestaurantes= datosRestaurantes + " Telefono "+ restaurante[4]
            datosRestaurantes= datosRestaurantes + "\n"
        linea=texto.readline()
    texto.close()
    return datosRestaurantes
