import web
from consultas import *
from flask import Flask, render_template, request, url_for

render = web.template.render('./templates/')
p = Prolog()

urls = (
    '/','index',
    '/','horario',
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
    '/horario','horario',
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

class platillos:
    def GET(self):
        return render.platillos()
    def POST(self):
        i = web.input()
        raise web.seeother('/platillos')

class busqueda:
        def GET(self):
                return render.busqueda()
	def POST(self):
		i = web.input()
        	raise web.seeother('/busqueda')

class agregar_platillo:
    def GET(self):
        return render.agregar_platillo()
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
        
class horario:
    def GET(self):
        return render.horario("Hola desde Python", "Bye", "14", "8", "25", "42", "19")
    def POST(self):
        i = web.input()
        raise web.seeother('/agregar_restaurante')

if __name__ == "__main__":
        app.run()
