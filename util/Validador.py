from flask import request,jsonify
from functools import wraps
from util.Firma import * 
firma = Firma()
#todo correcto 0
#Token is missing 1
#token is invalidg 2
def get_user_token():
    token = None
    if 'x-access-token' in request.headers:
        token = request.headers['x-access-token']

    if not token:
        return {'rta' : '1', 'message':'Token is missing'}

    mi_token = firma.verificar_firma(token)
    
    if mi_token['rta'] == 200:
        return {'rta' : '0', 'usuario' : mi_token['data']['usuario']}
    else:
        return {'rta' : '2', 'message':'Token is invalid'}

def validador_s_2(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        return f({'codigo':request.json['codigo'],'pass':request.json['pass']},*args,**kwargs)
    return decorated

def validador_s_3(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data_token = get_user_token()
        if data_token['rta'] != '0':
            return jsonify({'message':data_token['message'] }), 401
        else:
            return f(data_token['usuario'],request.json['sesion'],*args,**kwargs)
    return decorated

"""def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        #print request.headers
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        mi_token = firma.verificar_firma(token)
        #print "hola"
        #print mi_token
        
        if mi_token['rta'] == 200:
            usuario = mi_token['data']['usuario']
        else:
            return jsonify({'message' : 'Token is invalid!'}), 401

        snum = request.headers['S-Num'];
        if snum == '1':
            return f(usuario,*args,**kwargs)
        elif snum == '2':
            return f(usuario,*args,**kwargs)
        elif snum == '3':
            return f(usuario,request.json['sesion'],*args,**kwargs)
        else:
            return jsonify({'message' : 'suma no encontrada'}), 401

    return decorated"""