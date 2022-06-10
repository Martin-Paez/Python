"""------------------------------------------------------------------"""
""" IMPORTAR ARCHIVOS ---------------------------------------------- """
"""------------------------------------------------------------------"""
import os # para limpiar la pantalla
import sys
sys.path.append('./imports')
from historial import *	#Para arministrar los filtros (incluidos)
from lector	import * #Para interpretar los comandos, lee palabras
sys.path.append('./imports/google_sheet')
from googlesheet import * # Para acceder a google sheet (xls)
sys.path.append('./imports/modo_automatico')
from modo_automatico import *
import importlib

""" Instala una aplicacion. """
def install(soft):
	soft = importlib.import_module(soft, package=None)
	return soft.instalar()
	
"""------------------------------------------------------------------"""
""" MOSTRAR Y PEDIR DATOS -------------------------------------------"""
"""------------------------------------------------------------------"""

""" Imprime los registros de un modo amigable para el usuario. Si esta
	habilitado el modo_automatico guarda en un archivo los datos. """
def imprimir(registros, py):
	if( len(registros) == 0 ):
		print("No hay datos seleccionados")
		#print("Filtros aplicados: "+str(len_hist(py["hist"]))+"\n")
		return
		
	for fila in registros:
		values="| "
		for k in fila.keys():
			if(k!=""):
				values = values + k + ": " + str(fila[k]) + " | "
		print(values)
		if(py.get("auto_cmd") is not None):
			escribir_salidas(values, py["auto_path"])
	return

def imprimir_ayuda():
	print("\nMenu")
	print(" ? : Menu de comandos ")
	print(" s : para salir \n")

def imprimir_menu():
	opt = ""
	
	while ( opt.upper() != "7" ):
	
		os.system("cls")
	
		print("\n MENU: ")
		print("\n1) Seleccionar (Aplicar filtros)")
		print("2) Insertar / Eliminar")
		print("3) Mostrar datos")
		print("4) Operaciones matematicas")
		print("5) Administrar Google Sheet")
		print("6) Modo automatico")
		print("7) Salir\n")
		
		opt = input("Opcion: ")
		ok = True 
		
		if( opt in "1234567" ):
			os.system("cls")
			print("\n------------------ COMANDOS ----------------------")
			
		if( opt=="1") :
			
			print("\n---- SELECCIONAR DATOS (Aplicar FILTROS) ----------\n")
			print("f categoria [ > | < | = ] valor: Mayor/Menor(numeros) o Igual a un valor dado")
			print("max categoria: Maximos de una categoria numerica")
			print("min categoria: Minimos de una categoria numerica") 
			
			print("\n------------ ADMINISTRAR FILTROS ------------------\n")
			print("f -v: Mostrar historial de filtros aplicados")
			print("f -d: Quitar filtros")
			print("f -N: Elimina los ultimos N filtros")
					
		elif ( opt=="2") :
			
			print("\n---------- INSERTAR/ELIMINAR DATOS ----------------\n")
			print("i: Insertar fila en Google Sheet, se iran pidiendo los datos de a uno por vez")
			print("i col=val col=val ... : Deben estar todas las columnas")
			print("e: Eliminar de Goolge Sheet los datos de la seleccion actual")
			print("e -f: Idem comando 'e' pero sin pedir confirmacion")
			
		elif ( opt=="3") :
			
			print("\n------------ MOSTRAR DATOS ---------------\n")
			print("v: Ver seleccion actual")
			print("v -t: Ver todo el libro contable")
			#print("v -f categ valor categ valor...: Ver filtro sin modif. seleccion") 
			
		elif ( opt=="4") :
			
			print("\n----- OPERACIONES MATEMATICAS ------------\n")
			print("c: Contar elementos de la seleccion actual") 
			print("t categoria: Suma de una categoria numerica para la seleccion actual")
			print("p categoria: Promedio de una categoria numerica para la seleccion actual")
			
		elif ( opt=="5") :
				
			print("\n----  ADMINISTRAR GOOGLE SHEET -----------\n")
			print("h nombre_hoja: trabajar con otra hoja de calculo ")
			print("h -a: Mostrar el nombre de la hoja actual ")
			print("h -d nombre_hoja: Crea una hoja vacia con la tabla de la hoja activa ")
			print("h -d -f: Idem 'h -d', sin pedir confirmacion para sobreescribir una hoja preexistente")
			print("h -v: Mostrar todas las hojas")
			print("h -e nombre_hoja: Elimina una hoja (distinta de la hoja activa).")
			print("a: Sincronizar posibles modificaciones externas del archivo")

		elif ( opt=="6") :	
				
			print("\n---------- Modo Automatico ---------------\n")
			print("auto:  Ejecuta los comandos del archivo modo_automatico.txt y genera Salidad.txt")
			print("check: Encuentra diferencias entre Salidas.txt y Respuestas_Correctas.txt ")
			print("guardar salidas: Convierte Salidas.txt en Respuestas_Correctas.txt ")
			print("guardar salidas nombre_archivo: Convierte Salidas.txt en el archivo indicado ")
			print("guardar comandos: Sobreescribe modo_automatico.txt con los comandos del historial")
			print("guardar comandos nombre_archivo: Guarda los comandos del historial en el archivo indicado")
			print("borrar comandos: El primer comando del historial sera el proximo ingresado")
			print("borrar comandos N: Quita del historial los ultimos N comandos ingresados")
			print("mostrar comandos: Muestra los comandos usados, aun si sus parametros no eran correctos")
		
		elif ( opt == "7" ):
			ok = False
			os.system("cls")
			py["app_activa"]["ayuda"]()
		else:
			ok = False
			print("Ingrese un numero entre 1 y 7")
				
		if (ok):
			input("\nPresione Enter para volver")
		
	return	

""" Permite leer un comandos. Si esta habilitado el modo_automatico lee
	los comandos de la lista py["auto_cmd"], cargados desde un archivo
	al momento de habilitar dicho modo. De lo contrario se lo solicita 
	al usuario. """
def leer_comando(py):
	if(py.get("auto_cmd") is None): #py["auto_cmd"] : lista de comandos
		cmd = input(">> ")
	else:
		if(len(py["auto_cmd"])==0 or py["auto_cmd"][0].upper()=="FIN\n"):
			print("\n Fin del modo automatico.\n")
			del py["auto_cmd"]
			cmd=""
		else:
			cmd = py["auto_cmd"][0][:-1] #Saco el \n final
			py["auto_cmd"] = py["auto_cmd"][1:]
			print(">> "+cmd)
	return cmd
	

"""------------------------------------------------------------------"""
""" OPERACIONES MATEMATICAS -----------------------------------------"""
"""------------------------------------------------------------------"""

""" Suma todos los valores de la seleccion actual (o sea, los datos 
	perteneciente a la actual hoja de calculo que pasaron todos los 
	filtros) para una categoria dada. Si no contiene valores numericos 
	retorna -1. """
def sumar(py, categoria):
	s = 0
	for e in py["selec"]:
		try: #para chequear errores, en este caso si no es un numero
			num = float(e[categoria])
			s = s + num
		except: #si no es numero, viene aca
			return -1
	return s

""" Calcula el total/promedio de los datos seleccionados (o sea, los 
	datos perteneciente a la actual hoja de calculo que pasaron todos 
	los filtros), segun indique el comando recibido por parametro. """
def tot_prom(py, cmd, operacion):
	[cat, cmd]=sig_palabra(cmd)
	if ( not solo_espacios(cmd) ):
		py["app_activa"]["ayuda"]()
		return
	try:
		check_categoria(py["selec"], cat)
		operacion_txt = "Total"
		rta = sumar(py, cat)	
		if(rta==-1):
			print("Hay al menos un elemeno que no se puede sumar\n")
		else:
			if(operacion.lower()=="p"): 
				rta = rta / len(py["selec"])
				operacion_txt = "Promedio"
			print(operacion_txt+" de "+cat+": "+str(rta))

	except ValueError as txt:	
		print(txt)
	return py



"""------------------------------------------------------------------"""
""" SELECCIONAR DATOS (Aplicar FILTROS)------------------------------"""
"""------------------------------------------------------------------"""

""" Segun lo que indica el comando recibido por parametro , muestra los
	filtros del historial, quita todos los filtros, elimina los ultimos 
	N filtros o agrega el filtro indicado. """
def trabajo_con_filtros(py, cmd):
	[cat, cmd] = sig_palabra(cmd[2:]) #sintaxtis conveniente
#Muestro los filtros que se aplciaron
	catL = cat.lower()
	if(catL=="-v"): 
		imprimir_filtros(py["hist"])
#Elimino todos los filtros
	elif(catL=="-d"): 
		py["selec"]=py["regs"].copy()
		py["hist"]=nuevo_historial()
#Elimino los ultimos N filtros
	elif(len(cat)>0 and cat[0]=="-"): 
		n=0
		try:
			n = int(cat[1:])
		except:
			print("Comando Incorrecto\n")
		if(n>0):
			if(len_hist(py["hist"])<=n):
				trabajo_con_filtros(py,"f -d") #Elimino todos
			else:
				[py["hist"], py["selec"]] = quitar_filtros(py["hist"],n, py["regs"])
# Aplico un filtro
	else: 
		[cond, val, cmd]=leer_dos_argumentos(cmd)
		if(val == ""):
			print("Debe ingresar un valor. Por ejemplo cat > 1\n")
		elif(not solo_espacios(cmd)):
			print("Demasiados argumentos\n")
		else:
			try:
				py["selec"]=filtrar(cat,cond, val,py["selec"])
				py["hist"]=agregar_filtro(py["hist"],[filtrar,cat,cond,val])
			except ValueError as txt:	
				print(txt)
	return py

""" Calcula el minimo/maximo de una categoria dada para los datos 
	seleccionados (o sea, los datos pertenecientes a la actual hoja de
	calculo que pasaron todos los filtros), segun indique el comando
	recibido por parametro. """
def trabajo_con_min_max(py, cmd):
	[cond, cat, cmd]=leer_dos_argumentos(cmd) 
	try:
		py["selec"] = min_max(cat, cond, py["selec"])
		habilitar_filtrado_completo(py["hist"])	
		py["hist"]=agregar_filtro(py["hist"],[min_max,cat,cond])
	except ValueError as txt:	
		print(txt)
	return py
	
	
"""------------------------------------------------------------------"""
""" ELIMINAR/INSERTAR DATOS -----------------------------------------"""
"""------------------------------------------------------------------"""
	
""" Elimina los datos seleccionados, o sea, los datos pertenecientes
	a la actual hoja de calculo que pasaron todos los filtros. """
def eliminar_seleccionados(py, cmd):		
	s = leer_dos_argumentos(cmd)
	if(not solo_espacios(s[1])):
		py["app_activa"]["ayuda"]()
		return py
		
	check = "S"		
	if((s[0]=="-f" and s[1]=="") or s[0]==""):
		if (len(py["selec"])==0):
			print("No se aplica, ya que no hay elementos seleccionados\n")
			check = "N"	
		elif(s[0]==""):		
			para_borrar="lo seleccionado"
			if(py["selec"]==py["regs"]): #Si no hay filtros
				para_borrar="TODO"
			check = input("¿seguro quiere borrar " + para_borrar + " ?(S/N): ")
	else:
		py["app_activa"]["ayuda"]()
		check = "N"

	if( check.upper()=="S"):
		ok = False
		try:
			py["regs"] = eliminar(py["selec"],py["sheet"], py["regs"],py["delay"])
			ok = True
		except:
			print("Hubo problemas al intentar modificar la hoja de calculos")
		if (ok):
			py["selec"] = actualizar_seleccion_eliminada(py["hist"], py["regs"])
	return py
	
""" Escribe un dato en la hoja de calculo, es agregado a la seleccion 
	actual segun corresponda con el historial de filtros. """
def insertar_dato(py, lector, datos):
	ok = False
	reg = {}
	try:
		fila = len(py["regs"])+2
		reg=anotar(py["sheet"], lector, datos,py["delay"], fila)
		ok = True
	except:
		print("Hubo problemas al intentar modificar la hoja de calculos.")
	if (ok):
		py["regs"].append(reg)	#cumple enunciado 1)
		if(hay_filtros(py["hist"])):
			py["selec"] = actualizar_nuevo_registro(py["hist"], py["selec"], reg)
		else:
			py["selec"].append(reg)
	return py
	
""" Tienen el formato requerido por "anotar()" definida en 
	"googlesheet.py" . Su funcion es probeer los datos necesarios 
	para escribir en la hoja de calculo. """
def leer_de_lista(cat, datos):
	return datos[cat]

""" Su funcion es probeer los datos ingresados ppor el usuario. El 
	parametro "datos" esta presente para cumplir con la condicion 
	impuesta por anotar() definida en "googlesheet.py" . """
def leer_del_usuario(cat, datos):
	return input(cat+": ")
	
""" Inserta en la hoja de calcula un fila con la informacion 
	suministrada en el comando recibido por parametro, el cual debe
	contener informacion para cada una de las categorias. """
def insertar_por_comando(py, cmd): 
	datos = {}
	while(cmd != ""):
		[key,cmd] = sig_palabra(cmd)
		if (key!=""):
			[separador,val,cmd] = leer_dos_argumentos(cmd)
			if(separador == "=" and val!="" ):
				datos[key] = val
	py = insertar_dato(py, leer_de_lista, datos)
	return py


"""------------------------------------------------------------------"""
"""HOJAS DE GOOGLE SHEET --------------------------------------------"""
"""------------------------------------------------------------------"""

""" Es posible que se ingrese informacion a la hoja de calculo desde
	el navegador de interner, por ellos esta funcion permite sincronizar
	los datos con la nube. """
def sincronizar_hoja(py):
	ok = False
	try:
		py["regs"] = cargar_registros(py["sheet"])
		ok = True
	except:
		print("Hubo problemas leer los datos de la hoja")

	reservado = -1 * py["filas_reservadas"]
	py["regs"] = py["regs"][:reservado]

	if(ok):
		py["selec"] = py["regs"].copy()
	return py
	
def cambiar_delay(cmd):
	s = leer_dos_argumentos(cmd)
	if(s[1] == "" ):
		try:
			s[0] = float(s[0])
		except:
			py["app_activa"]["ayuda"]()
		
		i = "s"
		if(s[0]>2):
			i = input("¿Seguro que desea un delay tan grande?(S/N)")
		if(i.lower == "s"):
			py["delay"] = s[0]
	else:
		py["app_activa"]["ayuda"]()
				
""" Para elegir una hoja de calculo diferente, sobre la cual trabajar. """
def cambiar_hoja(py,nombre):
	if(py["sheet"].title == nombre):
		print("No es necesario cambiarla, " + nombre+ " ya es la hoja activa")
		return py
		
	ok = False
	try:
		py["sheet"] = seleccionar_hoja(py["xls"],nombre,py["delay"])
		ok = True
	except:
		print("Hubo problemas al intentar seleccionar la hoja. \n")
	
	if (ok):
		py = sincronizar_hoja(py)
		py["hist"]=nuevo_historial()
	return py
	
""" Crea una nueva hoja de calculo, carga en ella el formato de tabla
	utilizado en la hoja actual. Luego selecciona la nueva como actual. """
def cargar_tabla_vacia(py, nombre):
	ok = True
	forzado = False
	s = leer_dos_argumentos(nombre)
	if(s[0] == "-f"):
		forzado = True
		nombre = s[1]
	if ( nombre == py["sheet"].title):
		print("Debe elegir un nombre distinto al de la hoja activa\n")
		ok = False
	else:
		conect_ok = False
		try:
			sheets = todas_las_hojas(py["xls"],py["delay"])
			conect_ok = True
		except:
			print("Hubo problemas al intentar cargar la lista de hojas")
		
		if(conect_ok):
			cont = 0
			while( cont<len(sheets) and ok):
				if (nombre == sheets[cont].title):
					a = "S"
					if(not forzado):
						a = input("La hoja " + nombre + " existe, desea sobreescribir (S/N)")
					if (a.upper() == "S"):
						try:
							eliminar_hoja(py["sheet"],nombre, py["xls"], py["delay"])
						except:
							print("Hubo problemas al intentar sobreescribir la hoja")
							ok = False
					else:
						ok=False
				cont = cont + 1
	if(ok):
		crear_hoja(py["xls"], py["regs"], nombre, py["delay"])
		py = cambiar_hoja(py, nombre)
	return py

""" Interpreta el comando "guardar":
	
	Por un lado, se puede hacer una copia de respaldo de las salidas 
	generadas al habilitar el modo automatico.
	
	Por otro lado, es posible guardar en un archivo el historial de
	comando ingresados. """
def guardar_modo_auto(py, cmd):
	sig = leer_dos_argumentos(cmd)
	if (sig[0]=="salidas"):
		if(sig[1]==""): #Archivo Default
			f = "Respuestas_Correctas.txt"
		else:
			f = sig[1]
		guardar_respuestas_correctas(py["auto_path"], "Salidas.txt", f)
		py["hist_cmd"] = py["hist_cmd"][:-1]  #quito el comando "guardar"
	elif (sig[0]=="comandos"):
		if(sig[1]==""):
			f = "modo_prueba.txt"
		else:
			f = sig[1]
		py["hist_cmd"] = py["hist_cmd"][:-1] #quito el comando "guardar"
		guardar_comandos(py["auto_path"],py["hist_cmd"], f)
	else:
		py["app_activa"]["ayuda"]()
	return py

""" Interpreta los comandos: 
	borrar comandos - Limpia el historial de comandos
	borrar comandos N - Quita los ultimos N comandos del historial
	mostrar comandos - Muestra el historial de comandos """	
def hist_comandos(py,cmd):
	py["hist_cmd"] = py["hist_cmd"][:-1] #Desestima el comando que permitio llegar aca
	cmd = cmd.lower()
	[tarea, cmd] = sig_palabra(cmd)
	sig = leer_dos_argumentos(cmd)
	ok = False
	if (sig[0]=="comandos"):
		if(tarea == "borrar"):
			sig = leer_dos_argumentos(cmd)
			if(sig[1]==""):
				py["hist_cmd"] = []
				ok = True
			else:
				try:
					n = int(sig[1])
					py["hist_cmd"] = py["hist_cmd"][:-n] #si n>=len no pasa queda vacio
					ok = True
				except:
					print(n)
					None #Comando incorrecto, abajo imprimo para todos				
		elif(tarea == "mostrar" and sig[1]==""):
			len_h = len(py["hist_cmd"])
			for c in range(len_h): #el ultimo comando es el actual
				print(py["hist_cmd"][c])
			ok = True
			
	if(not ok):
		py["app_activa"]["ayuda"]()
	return py
	
""" Retorna el archivo xls , en caso de tener problemas para conectarse
	con el servidor, da la opcion al usuario de seguir intentado. """
def conectarse_a_google():
	path = "./imports/google_sheet/"
	xls = False
	i = "S"
	while (not xls and i.upper() != "N"):
		try:
			# True = Cualquier cosa distinta de 0 o False
			xls = cargar_xls(path,0)
		except:
			i = input("\n¿Desea intentar de nuevo? (S/N): \n")		

	return xls
	
def ejecutar_comando(cmd,py):
	cmdL = cmd.lower()
		
	if(sin_espacios_al_final(cmd,"?")):
		imprimir_menu()
#Insertar	
	elif(sin_espacios_al_final(cmdL,"i")):
		py = insertar_dato(py, leer_del_usuario, [])
	
	elif(cmdL[0:2]=="i "): 
		py = insertar_por_comando(py, cmd[2:]) 
#Filtrar
	elif(sin_espacios_al_final(cmdL,"f") or cmdL[:2]=="f "): # Filtrar y Mostrar filtros
		py = trabajo_con_filtros(py, cmd)

	elif((cmdL[:4]=="max " or cmdL[:4]=="min ")): # cumple enunciado 6)
		py = trabajo_con_min_max(py, cmd)
#Mostrar
	elif(sin_espacios_al_final(cmdL,"v")): # cumple enunciado 2)
		imprimir(py["selec"], py)
		
	elif(sin_espacios_al_final(cmdL,"v -t")):
		imprimir(py["regs"], py)
#Eliminar		
	elif(sin_espacios_al_final(cmdL,"e") or cmdL[:2]=="e "):
		py = eliminar_seleccionados(py, cmd[2:])
#Matematicas
	elif(sin_espacios_al_final(cmdL,"c")): # cumple enunciado 3)
		print("Elementos seleccinados: " + str(len(py["selec"]))+"\n")
		
	elif((cmdL[:2]=="t " or cmdL[:2]=="p ")): # cumple enunciado 7) y 3)
		tot_prom(py, cmd[2:], cmdL[0])
#Google Sheet			
	elif(sin_espacios_al_final(cmdL,"a")): #Actualizar valores de la hoja de google sheet
		py = sincronizar_hoja(py)
		
	elif(cmdL[:5]=="delay "):
		cambiar_delay(cmd[5:])
				
	elif(cmdL[:5]=="h -d "): #Duplicar hoja de google sheet
		py = cargar_tabla_vacia(py, cmd[5:])
			
	elif(sin_espacios_al_final(cmdL,"h -v")):
		imprimir_hojas(py["xls"], py["delay"])
			
	elif(sin_espacios_al_final(cmdL,"h -a")):
		print(py["sheet"].title)
		
	elif(cmdL[:5]=="h -e "):
		if (not eliminar_hoja(py["sheet"], cmd[5:], py["xls"],py["delay"]) ):
			print("No se puede eliminar la hoja actual\n")

	elif(cmdL[:2]=="h "): #Cambiar hoja de google sheet
		py = cambiar_hoja(py, cmd[2:])
	
	elif(cmdL[:2]=="r "):
		[filas, cmd]=sig_palabra(cmdL[2:])
		if(cmd!=""):
			py["app_activa"]["ayuda"]()
		else:
			try:
				py["filas_reservadas"] = int(filas)
			except:
				print("Se esperaba un numero")
		sincronizar_hoja(py)
#Modo Automatico						
	elif(sin_espacios_al_final(cmdL,"auto")):
		if(py.get("auto_cmd") is None): 
			py["hist_cmd"] = py["hist_cmd"][:-1]
			py["auto_cmd"] = habilitar_modo_automatico(py["auto_path"])
			
	elif(sin_espacios_al_final(cmdL,"check")):
		check_salidas(py["auto_path"])
		py["hist_cmd"] = py["hist_cmd"][:-1]
			
	elif(cmdL[:8]=="guardar "):
		py = guardar_modo_auto(py, cmdL[8:])
			
	elif(cmdL[:7]=="borrar " or cmdL[:8]=="mostrar "):
		py = hist_comandos(py,cmdL)
		
	elif(cmdL[:9]=="instalar "):
		[soft, cmd] = sig_palabra(cmd[9:])
		if (solo_espacios(cmd)):
			py["apps"][soft]=install(soft)
			try:
				None
			except:
				print("No se pudo instalar. Tenga en cuenta que el programa debe estar en el directorio principal")
				
	elif(cmdL[:9]=="ejecutar "):
		[soft, cmd] = sig_palabra(cmd[9:])
		if (solo_espacios(cmd) and py["apps"].get(soft) is not None):
			[leer, ayuda, ejecutar] = py["apps"][soft]
			py["app_activa"] = py["apps"][soft]
			estado_previo = py
			py["app_activa"]["ejecutar"](py)
			py["app_activa"] = py["apps"]["principal"]
			py = estado_previo
		else:
			py["app_activa"]["ayuda"]()
#Ayuda	
	else:
		py["app_activa"]["ayuda"]()
		py["hist_cmd"] = py["hist_cmd"][:-1]
		
	
def programa():
	xls = conectarse_a_google()
	if (xls) :			
		#El diccionario py es mi programa en si, o sea toda la informacion
		py={"xls":xls,"hist":nuevo_historial(),"sheet":"","regs":[],"selec":[]}
		py["auto_path"] = "./imports/modo_automatico/"
		py["hist_cmd"] = []
		py["delay"] = 0.2
		py["app_activa"] = {"leer":leer_comando,"ayuda":imprimir_ayuda}
		py["app_activa"]["ayuda"]()
		py["apps"] = {"principal":py["app_activa"]}
		py["run_cmd"] = ejecutar_comando
		py["filas_reservadas"]=0
		sheets = todas_las_hojas(xls,py["delay"])
		cmd="h "+sheets[0].title #Cargo la primer hoja por defecto
		while(cmd != "s" and not (cmd[0] == "s" and solo_espacios(cmd[1:]))):
			ejecutar_comando(cmd,py)
			cmd = ""
			while(cmd==""):
				cmd = py["app_activa"]["leer"](py)
			cmd = cmd[espacios_al_comienzo(cmd):]
			py["hist_cmd"].append(cmd)
			
	return

programa()
