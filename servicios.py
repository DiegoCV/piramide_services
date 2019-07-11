servicios = {
	's_1':{
		'ruta':'/vendedor/registrar'
	},
	's_2':{
		'ruta':'/vendedor/verificar'
	},
	's_3':{
		'ruta':'/sesion/agendar'
	}
} 

def ruta(servicio):
	return servicios[servicio]['ruta']