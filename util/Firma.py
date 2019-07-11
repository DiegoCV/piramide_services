import jwt
import datetime
class Firma():
	def __init__(self):
		self.mi_key = 'No vives de ensalada'

	def verificar_firma(self,firma):
		try: 
			firma_aux = jwt.decode(firma, self.mi_key)
			if firma_aux['nort'] == 'coding':
				return {'rta' : 200,'data':firma_aux}
			else:
				return {'rta' : 401}
		except:
			return {'rta' : 402}

	def obtener_firma(self,usuario):
		token = jwt.encode({'usuario' : usuario, 'nort':'coding','exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, self.mi_key)
		token.decode('UTF-8')
		return token