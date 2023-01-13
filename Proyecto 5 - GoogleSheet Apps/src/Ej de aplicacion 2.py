import os

def leer(py):
	return input("> ")

def menu():
	print("\nCOMANDOS:\n")
	print("i : ingresar todas las denominaciones")
	#print("i billete=cantidad billete=cantidad ... : ingresar cantidades de algunas denominaciones")
	print("t : total")
	print("b : Balance") 
	print("s : Salir") 
	
def ejecutar(py):
	os.system("cls")
	py["run_cmd"]("h Calc",py)
	py["run_cmd"]("r 2",py)
	opt=""
	while (opt != "s"):
		py["run_cmd"]("f -d",py)
		if (opt == "i"):
			py["run_cmd"]("i",py)	
			if(len(py["selec"])>0):
				cmd = "i"
				for k in py["selec"][0].keys():
					if(k!="" and k!="Fila"):
						cmd = cmd + " " + k + "="
						cmd = cmd + str(int(py["selec"][0][k]) + int(py["selec"][1][k])) 
				py["run_cmd"]("e -f",py)
				py["run_cmd"](cmd,py)
				try:
					None
				except:
					print("Los datos ingresados deben ser numericos")
		if (opt == "i"):
			py["run_cmd"]("",py)	
			
			else:
			menu()
		opt = input("> ")
		opt = opt.lower()
	
def instalar():
	app = {"leer": leer, "ayuda":menu, "ejecutar":ejecutar}		
	return app

