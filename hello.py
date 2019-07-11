from flask import Flask, request, abort, jsonify, make_response
from util.Validador import validar,token_required
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

@app.route(ruta('s_2'), methods=['GET'])
def verificarVendedor():
    if validar(ruta('s_2'),request):
        #Aqui deberia ir el llamado al controlador
        return reponder()
    else:
        return responderError()

#@validar Aqui deberiamos validar la estrucrura del json que llega
@app.route(ruta('s_3'), methods=['GET'])
@token_required
def agendar_sesiones(vendedor,sesion):
    if insertarSesion(vendedor,sesion):
        #Aqui deberia ir el llamado al controlador
        return reponder()
    else:
        return responderError()

#Metodo ficticio, hay que reemplazar por el cintrolador
def insertarSesion():
    return 1
app.run()