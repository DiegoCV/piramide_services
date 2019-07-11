from flask import Flask, request, abort, jsonify, make_response
from util.Validador import *
from util.Pregonero import * 
from servicios import ruta

app = Flask(__name__)

@app.route(ruta('s_1'), methods=['GET'])
def registrarVendedor():
    if validar(ruta('s_1'),request):
        #Aqui deberia ir el llamado al controlador
        return reponder()
    else:
        return responderError()

@app.route(ruta('s_2'), methods=['POST'])
@validador_s_2
def verificarVendedor(vendedor):
    if login(vendedor):
        usuario = {'codigo':vendedor['codigo'],'id':'01'}
        return reponderLogin(usuario)
    else:
        return responderError()


@app.route(ruta('s_3'), methods=['POST'])
@validador_s_3
def agendar_sesiones(usuario,sesion):
    if insertarSesion(sesion):
        #Aqui deberia ir el llamado al controlador
        return reponderTEST(usuario,sesion)
    else:
        return responderError()


#Metodo ficticio, hay que reemplazar por el cintrolador
def insertarSesion(sesiones):
    return 1

def login(user):
    if user['codigo'] == 'admin' and user['pass'] == 'admin':
        return 1
    return 0
app.run()