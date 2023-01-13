""" Para eliminar y copiar archivos """
import os
from shutil import copyfile

def habilitar_modo_automatico(path):
	lines=[]
	try:
		f = open(path+"modo_prueba.txt","r")
		lines = f.readlines()
		f.close
		f = open(path+"salidas.txt","w+")
		f.truncate(0)
		f.close()
	except:
		print("\n No se pudo habilitar el modo automatico.")
		print("Asegurese de que existe el archivo modo_prueba.txt en el directorio.\n")
	return lines
	
def escribir_salidas(values, path):
	try:
		f = open(path+"salidas.txt","r")
		num_linea = len(f.readlines())
		f.close()
		f = open(path+"salidas.txt","a")
		f.write(str(num_linea)+") "+values+"\n")
		f.close()
	except:
		print("Error con el archivo Salidas.txt")

def check_salidas(path):
	s=""
	c=""
	try:
		s = open(path+"salidas.txt","r")
	except:
		print("No se encuentra el archivo Salidas.txt\n")
	try:
		c = open(path+"Respuestas_Correctas.txt","r")
	except:
		print("No se encuentra el archivo: Respuestas_correctas.txt\n")
	if( s!="" and c!=""):
		s_lines=s.readlines()
		c_lines=c.readlines()
		s.close()
		c.close()
		s_len = len(s_lines)
		c_len = len(c_lines)
		ok=True
		if(s_len != c_len):
			if(c_len<s_len):# me quedo con el menor en s_len
				s_len=c_len
			print("Diferente cantidad de lineas")
			ok = False
		elif(s_len==0): #si llegue aca, s_len==c_len
			print("Los archivos no contienen informacion\n")
			ok = False
		count = 0
		while(count<s_len): #en s_len tengo el minimo de lineas
			if (s_lines[count] != c_lines[count]):
				ok = False
				print("Diferencias encontradas en linea " + str(count))
			count = count+1
		if(ok):
			print("Prueba Exitosa")
			
def guardar_respuestas_correctas(path, nombre_origen, nombre_destino):
	try:
		os.remove(path+nombre_destino)
	except:
		None
	try:
		copyfile(path+nombre_origen,path+nombre_destino)
	except:
		print("Hubo un problema al copiar el archivo")

def guardar_comandos(path, lines, nombre_archivo):
	try:
		f = open(path+nombre_archivo,"w+")
		for cmd in lines:
			f.write(cmd+"\n")
		f.close()
	except:
		print("Hubo problemas con el archivo " + nombre_archivo)
