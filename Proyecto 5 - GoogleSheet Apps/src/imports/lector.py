def no_es_separador(string):
	ok = string!=" " and string!="=" 
	ok = ok and string!="<" and string!=">"
	return ok
	
def contiene_varias_palabras(string):
	ok=False
	if((" " in string) or ("=" in string)):
		ok = True
	elif((">" in string)or ("<" in string)): #para hacerlo mas corto
		ok = True
	return ok
	
""" Retorna la primer palabra del string. Si no es posible retorna un 
	string vacio. 
	Se considera a los signos =,> y < como el final o comienzo de una 
	palabra, asi como una palabra en si mismo. 
	Por ejemplo: 2=1+1 se considera como tres palarabas: el 2, el = y 
	el 1+1. """
def sig_palabra(string):
	resto=""
	palabra = string
	if(len(string)>0):
		c=espacios_al_comienzo(string)
		if(c==len(string)): #Solo enviaron espacios
			palabra = ""
		else:
			d=c
			if(string[d] in "= > <"):
				palabra=string[d]
				resto = string[d+1:]
			elif(contiene_varias_palabras(string[d:])):
				while(no_es_separador(string[d])):
					d = d+1
				palabra = string[c:d]
				resto=string[d:]
			else: #Ultima palabra
				palabra = string[c:]
	return [palabra,resto]

""" Retorna en una lista las primeras dos palabras del string. """
def leer_dos_argumentos(string):
	ok=False
	b=""
	cmd=""
	[a,b]= sig_palabra(string)
	if(a!=""):
		[b,cmd] = sig_palabra(b)
	return [a,b,cmd]

""" Retorna True si el string esta compuesto solamente por espacios y/o
	tabulaciones. """
def solo_espacios(string):
	ok=True
	if(len(string)>0):#Elimino espacios
		cont=0
		while(cont<len(string) and (string[cont]==" " or string[cont]=="\t")):
			cont=cont+1
		if(cont<len(string)):
			ok=False
	return ok
	
""" Retorna la posicion del primer digito del string o el largo de la 
	cadena en caso de solo contener espacios. """
def espacios_al_comienzo(string):	
	c = 0
	while(c<len(string) and string[c]==" "): 
		c=c+1
	return c
	
""" Retorna True si el comando es igual a check_val, o bien es igual a
	check_val seguido solamente por espacios y tabulaciones. """
def sin_espacios_al_final(cmd, check_val):
	len_val = len(check_val)
	return cmd[:len_val]==check_val and solo_espacios(cmd[len_val:]) 
	
