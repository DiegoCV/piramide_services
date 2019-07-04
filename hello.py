from flask import Flask, request, abort, jsonify, make_response
from util.Firma import * 
import jwt
firma = Firma()

def validar_request(mi_request):
    return 1

app = Flask(__name__)
app.config['SECRET_KEY'] = 'No vives de ensalada'

@app.route('/vendedor/registrar', methods=['POST'])
def registrarVendedor():
    rta = validar_request(request)
    if not rta == 1:
        abort(rta)
    else:
        print(request.json['firma'])
    return jsonify(request.json)

@app.route('/a')
def hellof():
    encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
    return jsonify(jwt.decode(encoded, 'secret', algorithms=['HS256']))
    
@app.route('/b', methods=['POST'])
def hellofg():
    if firma.verificar_firma(request.json['firma']):
        return 'ok'
    else:
        return 'nook'
    
app.run()