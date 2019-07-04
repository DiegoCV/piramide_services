import jwt
class Firma():
	def __init__(self):
		self.mi_key = 'No vives de ensalada'
		
	def verificar_firma(self,firma):
		firma_aux = jwt.decode(firma, self.mi_key, algorithms=['HS256'])
		return firma_aux['nort'] == 'coding'
		
	def obtener_firma(self,firma):
		firma_aux = jwt.decode(firma, self.mi_key, algorithms=['HS256'])
		return firma_aux['nort'] == 'coding'