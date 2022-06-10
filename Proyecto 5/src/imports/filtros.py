from datetime import datetime 

""" Funciones condicion, para dar versatilidad a los filtros """
def menor(a,b):
	return a<b
def igual(a,b):
	return a==b
def mayor(a,b):
	return a>b
def contiene(a,b):
	return b in a

""" Retorna la condicion, que puede ser aplicable en los filtros, de 
	a cuerdo al string recibido. 
	Se aceptan los siguientes valores: > , < , =
	En caso de recibir otro valor retorna False. """	
def traducir_condicion(condicion):
	if(condicion==">" or condicion=="max"):
		condicion=mayor
	elif(condicion=="<" or condicion=="min"):
		condicion=menor
	elif(condicion=="="):
		condicion=igual
	elif(condicion=="contiene"):
		condicion=contiene
	else:
		raise ValueError("Operacion incorrecta. Se acepta: >, <, =, min, max\n")
	return condicion
	
""" Si la categoria no existe o la seleccion esta vacia da error con la
	descripcion correspondiente. """
def check_categoria(seleccion, cat):
	if (len(seleccion)==0):
		raise ValueError("No hay elementos seleccionados que filtrar\n")
	if (seleccion[0].get(cat) is None):
		raise ValueError("Categoria invalida\n")
		
"""	Retorna una lista con los regitros (diccionarios) en los cuales 
	el valor de la columna "categoria" y el parametro "valor"
	cumplen con la funcion "condicion": igual(), menor() o mayor().
	
	Da error si la seleccion esta vacia, la categoria es invalida, si la 
	condicion esta mal (distinto de: <, >, =) o si hay en dicha categoria
	al menos un dato no numerico para las condiciones mayor y menor. """
def filtrar(categoria, condicion, valor, seleccion):	
	check_categoria(seleccion, categoria)
	condicion = traducir_condicion(condicion)
	filtro = []
	formato = valor.count("/")
	if(formato==0 or formato > 2):
		es_fecha = False
	else:
		if(formato == 1):
			fecha_actual = datetime.now()
			posible_fecha = valor + "/" + str(fecha_actual.year)
			print(posible_fecha)
		try:			
			posible_fecha = datetime.strptime(posible_fecha, '%d/%m/%Y')
			valor = posible_fecha
			es_fecha = True
		except:
			es_fecha = False
	for r in seleccion :
		if(es_fecha):
			try:
				r_val =  datetime.strptime(r[categoria], '%d/%m/%Y')
			except:
				raise ValueError("Se esperaba una fecha en la fila:" + str(r["Fila"])+"\n")
		else:
			try:	
				if(condicion == igual or condicion == contiene):
					valor = str(valor)
					r_val = str(r[categoria])
				else:
					valor = float(valor)
					r_val = float(r[categoria])
			except:
				raise ValueError("Error de tipos en la fila:" + str(r["Fila"])+"\n")
		if(condicion(r_val,valor)):
			filtro.append(r)
	return filtro
	
""" Retorna una lista con los registros (filas ,almecenadas en el 
	parametro seleccion) que contienen el maximo (cuando la condicion es 
	la funcion mayor()) o el minimo (cuando la condicion es la fucion
	menor()) de la categoria indicada. 

	Da error si la seleccion esta vacia, la categoria es invalida , si 
	la condicion esta mal (distinto de: min, max) o si en dicha 
	categoria se encuentra al menos un dato no numerico. """
def min_max(categoria, condicion, seleccion):
	check_categoria(seleccion, categoria)
	condicion = traducir_condicion(condicion)
	filtro = [seleccion[0]]
	s=1
	while( s<len(seleccion) ):
		r = seleccion[s]
		try:
			a = float( r[categoria] )
			b = float( filtro[0][categoria] )
		except:
			raise ValueError("Error de tipos, deberian ser solo numeros\n")
		if(condicion(a,b)):
			filtro = [r]
		elif(a==b):
			filtro.append(r)
		s=s+1
		
	return filtro
