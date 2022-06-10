""" Para trabajar con google sheet """
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
	
""" Retorna la hoja del archivo de google sheet que contiene el libro 
	contable.
	El path debe terminar con "/" , y el parametro t indica el tiempo
	de espera despues de comunicarse con el servidor. """
def cargar_xls(path, t):
	json = path + "iron-cedar-331617-6743037a3a9f.json"
	nombre_archivo = "python_goolge_sheet"
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
	client = gspread.authorize(creds)
	xls = client.open(nombre_archivo) #no haria falta un "close()"
	time.sleep(t)
	return xls

def seleccionar_hoja(xls, nombre_hoja, t):
	sheet = xls.worksheet(nombre_hoja)
	time.sleep(t)
	return sheet
	
def todas_las_hojas(xls, t):
	sheet = xls.worksheets()
	time.sleep(t)
	return sheet
	

def eliminar_hoja(actual, para_borrar, xls, t):
	rta = True
	sheet = xls.worksheet(para_borrar) #si no existe la crea
	if(para_borrar != actual.title):
		xls.del_worksheet( sheet )
		time.sleep(t)
		rta = False
	return rta 	

def imprimir_hojas(xls, t):
	for w in xls.worksheets():
		print(w.title)
	time.sleep(t)

""" Crea una nueva hoja llamada nuevo_nombre, dentro del archivo xls, 
	que contiene una tabla, vacia, respetando el formato de los 
	registros recibidos. 
	El parametro t, en segundos, establece un delay despues de cada 
	interaccion con el servidos. """
def crear_hoja(xls, registros, nuevo_nombre, t):
	if(len(registros)>0):
		cols = str(len(registros[0]))
		sheet = xls.add_worksheet(title=nuevo_nombre, rows=1, cols=cols)
		time.sleep(t)
		categorias = registros[0].keys()
		col = 1
		for c in categorias:
			sheet.update_cell(1,col,c)
			time.sleep(t)
			col = col+1
		sheet.update_cell(1,col-1,"")
		time.sleep(t)
		fil = 2
	else:
		xls.add_worksheet(title=nuevo_nombre,rows=1, cols=1)
		time.sleep(t)
		
	return
	
def enum_filas(seleccion, primer_fila):
	for r in seleccion:
		r["Fila"] = primer_fila
		primer_fila = primer_fila + 1
	return seleccion

""" Retorna una lista de diccionarios, cuyas key son
las categorias (titulo de las columnas) del libro contable 
(tabla de la hoja de google sheet) """
def cargar_registros(libro_contable):
	registros = libro_contable.get_all_records()
	registros = enum_filas(registros, 2)
	return registros

""" Retorna un registro(diccionario) con la nueva entrada despues de 
	anotarla en la hoja de calculo. Retorna None en caso de no ser 
	posible completar la accion, sin modificar la hoja de calculo.
	Los posibles problemas tienen que ver con el servidor o porque la
	funcion lector() no pudo leer correctamente alguno de los datos.

	La funcion que recibe como parametro, debe tener la siguiete 
	estructura: 
		lector(categoria, datos) 
	La misma debe retornar los valores que seran agregados a una nueva
	fila de la hoja de google sheet (sheet).

	 """
def anotaro(sheet, lector, datos, t):
	col = 1
	fil = len(sheet.col_values(1))+1
	time.sleep(t)
	categorias = sheet.row_values(1)
	registro={}
	sheet.add_rows(fil)#me aseguro que halla una fila
	time.sleep(t)
	try:
		for k in categorias:
			if(k!=""):
				valor = lector(k, datos)	
				sheet.update_cell(fil,col,valor)
				time.sleep(t)	
				registro[k]= valor#en programa() cumple enunciado cargando lista
				col=col+1
		registro["Fila"] = fil
	except:
		sheet.delete_rows(fil)
		time.sleep(t)
		raise ValueError()
		
	return registro

def anotar(sheet, lector, datos, t, fil):
	col = 1
	time.sleep(t)
	categorias = sheet.row_values(1)
	registro={}
	sheet.add_rows(fil)#me aseguro que halla una fila
	time.sleep(t)
	valores = []
	try:
		for k in categorias:
			if(k!=""):
				valor = lector(k, datos)	
				valores.append(valor)
				time.sleep(t)	
				registro[k]= valor#en programa() cumple enunciado cargando lista
				col=col+1
		sheet.insert_row(valores,fil)
		registro["Fila"] = fil
	except:
		raise ValueError()
		
	return registro

""" Elimina de la hoja de google sheet (libro_contable)
los registros almacenados en "seleccion" y retorna la lista actualizada
de registros

Nota: Se espera que en la lista seleccion los elementos esten ordenados
segun el numero de filas menor a mayor. Es importante que esten ordenados
porque al borrar de la hoja de calculo cambian los numeros de las filas
por debajo de la que es eliminada. """
def eliminar(seleccion, libro_contable, registros, t):
	c=len(seleccion)
	if ( c>0 ):
		if(seleccion==registros):
			libro_contable.delete_rows(2,c+1) #borro todo
			time.sleep(t)
			registros=[]
		else:
			menor_fila = seleccion[0]["Fila"] #los cambios se realizan de esta fila hacia abajo
			while(c>0):
				libro_contable.delete_rows(seleccion[c-1]["Fila"])
				time.sleep(t)
				registros.remove(seleccion[c-1])#los diccionarios no son copias, son los mismos 
				c=c-1 #empiezo del final, leer descripcion de la funcion
			actualizado=enum_filas(registros[menor_fila-2:],menor_fila)#la primer fila de datos en el google sheet vale 2
			registros=registros[:menor_fila-2] + actualizado
	return registros #Para cumplir con lo visto en la materia
