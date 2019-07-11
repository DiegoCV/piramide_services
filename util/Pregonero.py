from flask import jsonify

def reponder(self):
	return jsonify({'status' : '1','message':'Al parecer no eres tan malo despues de todo'})

def responderError(self):
	return jsonify({'status' : '0','message':'Tienes un mal dia'})
