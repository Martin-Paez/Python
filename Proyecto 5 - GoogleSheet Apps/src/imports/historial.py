from filtros import *

""" Crea un nuevo historial, o sea, una lista con dos elementos. El primero,
	es un string que determina el modo de filtrado: filtrado_completo o 
	filtro_simple (por defecto); el segundo, una lista cuyos elementos
	son listas con la informacion necesaria para aplicar cada filtro, en
	el orden establecido por su posicion en la misma. """
def nuevo_historial():
	historial = [[],[]]
	return habilitar_filtro_simple(historial)

def len_hist(historial):
	return len(historial[1])

""" Agrega un filtro al historial. El filtro debe ser una lista con la 
	informacion necesaria para aplicarlo. Se aceptan los siguientes 
	formatos:
	["min_max",categoria,condicion]
	["filtrar",categoria,condicion,valor] """	
def agregar_filtro(historial, filtro):
	historial[1].append(filtro)
	return historial
	
""" Retorna True si hay filtros en el historial. """
def hay_filtros(historial):
	return len(historial[1])>0
	
""" Las siguientes dos funciones son para unificar en un solo lugar 
	la marca con la cual se va a identificar el modo de filtrado. """
def marca_de_filtro_simple():
	return "aplicar solo al nuevo"
def marca_de_filtrado_completo():
	return "aplicar a toda la seleccion"
	
""" Habilita el modo filtrado_completo, que permite aplicar el historial
	de filtros al nuevo registro en conjunto con los demas.
	Es util para historiales que guardan filtros tales como: minimos o 
	maximos, ya que, como la comparacion es entre diferentes registros,
	el resultado de la operacion depende del valor de cada uno, y por
	lo tanto es necesario volver a aplicar a todos nuevamente en 
	conjunto. 
	Cabe destacar que, ante una insercion, NO es necesario aplicar el 
	historial al Universo completo, solamente, a la seleccion actual. 
	Sin embargo, ante la eliminacion de una seleccion completa, SI es 
	necesario calcular sobre el Universo en su totalidad. 
		
	Ejemplo, filtro_completo:
		registros = [1,2,4,5]
		historial = [max]  =>  seleccion = [5]
		
		Caso A: Al inserta 6, se aplica el historial sobre [5,6], 
		quedando la Seleccin = [6]
		 
		Caso B: Despues de eliminar el 5, es necesario aplicar al 
		Universo completo [1,2,4], quedando la Seleccion=[4]  """
def habilitar_filtrado_completo(historial):
	historial[0]= marca_de_filtrado_completo()
	return historial
	
""" Retorna True si el modo filtrado_completo esta habilitado """
def es_filtrado_completo(historial):
	return historial[0]== marca_de_filtrado_completo()
	
""" Retorna True si el modo filtro_simple esta habilitado. Estos filtros
	se caracterizan por emplear un valor de referencia , por lo tanto
	el resultado de la operacion sobre un registro puntual no depende
	del valor que tengan los demas. Por ello, por un lado, al realizar 
	una insercion basta con aplicar el historial sobre el nuevo valor; y
	por el otro, al eliminar un registro la Seleccion resultante es nula.
	
	Ejemplo, filtro_simple:  
		registros = [1,2,4,5]
		historial = [>1, <5]  =>  seleccion = [2,4]
		
		Caso A: Al inserta 3, se aplica el historial sobre 3, el cual 
		pasa y por lo tanto Seleccin = [2,3,4]
		
		Caso B: Despues de eliminar [2,4], no es necesario aplicar el
		historial quedando la Seleccion =[] """
def es_filtro_simple(historial):
	return historial[0]==marca_de_filtro_simple()

""" Habilita el modo filtro_simple. """
def habilitar_filtro_simple(historial):
	historial[0]=marca_de_filtro_simple()
	return historial
	
""" Dado un historial, determina cual debe ser el conjunto de registros
	que seran afectados por el historial de filtros, en caso de ser
	aplicado. La decision depende del modo vigente: filtrado_completo 
	(se aplica a toda la seleccion y al nuevo registro), o filtro_simple
	(solo aplica al nuevo). """
def crear_target(historial, seleccion, nuevo_reg):
	target=[]
	if(es_filtrado_completo(historial)): 
		target=seleccion.copy()
	target.append(nuevo_reg)
	return target
	
""" Aplica los filtros, en el orden preestablecido, a los registros 
	de la lista target """
def aplicar_filtros_anidados(target, filtros):
	j=0
	while(len(target)>0 and j<len(filtros)):
		if(filtros[j][0]==min_max):
			target=min_max(filtros[j][1],filtros[j][2],target)
		elif(filtros[j][0]==filtrar):
			target=filtrar(filtros[j][1],filtros[j][2],filtros[j][3],target)
		else:
			print("Error al recuperar los filtros")
		j=j+1
	return target

""" Ante un nuevo registo, le aplica los filtros del historial en el orden
 preestablecido. Si esta seteado el modo filtro_completo volvera a aplicar
 los filtros, al mismo tiempo, a todos los elementos de la seleccion actual.
 (necesario si se utilizo, por ejemplo, min_max). De lo contrario, con
 filtro_simple, solo se testea el nuevo registro, y, en caso de pasar los
 filtros, se agrega a la seleccion actual. 
 
 NOTA: Además del nuevo registro, no es necesario contemplar el Universo
  completo, basta con volver a filtrar la seleccion actual, o sea, el 
  resultado de aplicar el historial de filtros al universo mencionado. 
  
  Por ejemplo: Si U es el conjunto de todos los registros y f() un filtro
  anidado, entonces S=f(U) (siendo S una seleccion). 
  Al incorporar un nuevo registro r, basta con aplicar, f(S) y f(r). """
def actualizar_nuevo_registro(historial,seleccion,nuevo_reg):
	target=crear_target(historial,seleccion,nuevo_reg)
	resultado=aplicar_filtros_anidados(target,historial[1])
	if(es_filtro_simple(historial)):
		if(len(resultado)>0):
			seleccion.append(resultado[0])
		resultado = seleccion
	return resultado 

def quitar_filtros(historial, n, registros):
	if (n>len(historial[1])):
		n = 0
	else:
		n = len(historial[1])-n
	historial[1] = historial[1][:n]
	seleccion = aplicar_filtros_anidados(registros,historial[1])
	return [historial,seleccion]
	
""" Despues de eliminar una seleccion del Universo de registros puede
	que resulte necesario actualizar el valor de la nueva seleccion 
	resultante teniendo en cuenta los filtros del historial. 
	Si se trata del modo filtro_simple, estamos hablando de un conjunto 
	de filtros que se aplican a cada elemento utilizando un valor de 
	referencia. Dicho en otras palabras, la operacion de filtrado de un
	registro no guarda relacion con el valor de los demas, y por lo 
	tanto, despues de eliminados, la seleccion resultante es nula, o sea
	sin elementos (el resto, seguro, no pasa el filtrado).
	Por otra parte, si estamos en presencia de un filtro_completo, o sea
	que se aplicaron funciones, como min_max, cuya operatoria es el 
	resultado de comparar entre si distintos registros, se vuelve a 
	aplicar el historial de filtros sobre el total de registros para 
	obtener dicha seleccion resultante de eliminar los elementos de la 
	anterior. """
def actualizar_seleccion_eliminada(historial,registros):
	if(es_filtro_simple(historial)):
		seleccion = []
	else:
		seleccion = aplicar_filtros_anidados(registros,historial[1]) 
	return seleccion
	
def imprimir_filtros(historial):
	txt=""
	for f in historial[1]:
		if(f[0]==min_max):
			print(f[2]+" de "+str(f[1]))
		elif(f[0]==filtrar):
			print(str(f[1])+str(f[2])+str(f[3]))
			
