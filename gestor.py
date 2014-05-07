import web
from consultas import *
from flask import Flask, render_template, request, url_for

render = web.template.render('./templates/')
p = Prolog()
global rest1
rest1 = ""

urls = (
    '/','index',
    '/','agregar_restaurante',
    '/','consulta',
    '/','menu_agregar',
    '/','agregar_platillo',
    '/','restaurantes',
    '/','platillos',
    '/','busqueda',
    '/agregar_restaurante','agregar_restaurante',
    '/consulta','consulta',
    '/restaurantes','restaurantes',
    '/platillos','platillos',
    '/busqueda','busqueda',
    '/agregar_platillo','agregar_platillo',
    '/menu_agregar','menu_agregar',
    '/resultado_platillos','resultado_platillos'
)

app = web.application(urls,globals())

class index:
    def GET(self):
        return render.index()

class menu_agregar:
    def GET(self):
        return render.menu_agregar()
    def POST(self):
	i = web.input()
        raise web.seeother('/agregar_restaurante')

class consulta:
    def GET(self):
        return render.consulta()
    def POST(self):
        i = web.input()
        raise web.seeother('/consulta')


class restaurantes:
    def GET(self):
        dato = obtenerRestaurantes()
        return render.restaurantes(dato)
    def POST(self):
        i = web.input()
        datos = consultas.consulta()
        raise web.seeother('/restaurantes')

class resultado_platillos:
    def GET(self):
        listaRestaurante = []
        lista = obtenerPlatilloRest(rest1)
        print lista
        return render.platillos(listaRestaurante,lista)
    def POST(self):
        i = web.input()
        raise web.seeother('/platillos')
        
class platillos:
    def GET(self):
        listaRestaurante = listaRestaurantes()
        lista = []
        return render.platillos(listaRestaurante,lista)
    def POST(self):
        i = web.input()
        rest1 = i.txtRestaurante
        raise web.seeother('/resultado_platillos')

class busqueda:
        def GET(self):
                return render.busqueda()
	def POST(self):
		i = web.input()
        	raise web.seeother('/busqueda')

class agregar_platillo:
    def GET(self):
        lista = listaRestaurantes()
        return render.agregar_platillo(lista)
    def POST(self):
        i = web.input()
        restaurante=i.txtRestaurante
        platillo=i.txtPlatillo
        tipo=i.tipos
        pais=i.pais
        ingredientes=i.ingredientes
        listaIngredientes = "["+ingredientes+"]"
        agregarPlatillo(restaurante,platillo,tipo,pais,listaIngredientes)
        raise web.seeother('/agregar_platillo')

class agregar_restaurante:
    def GET(self):
        return render.agregar_restaurante()
    def POST(self):
        i = web.input()
        nombre=i.txtNombre
        comida=i.txtComida
        ubicacion=i.txtUbicacion
        telefono=str(i.txtTelefono)
        agregarRestaurante(nombre,comida,ubicacion,telefono)
        raise web.seeother('/agregar_restaurante')

if __name__ == "__main__":
        app.run()
