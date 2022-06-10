import os

def leer(py):
	return input("> ")

def menu():
	print("\nMENU:\n")
	print("1)Cargar dato")
	print("2)Mostrar datos de alumnos aprobados")
	print("3)Cantidad de alumnos aprobados")
	print("4)Mostrar Alumnos de una Materia") 
	print("5)Ver si un determinado alumno tiene al menos una materia asignada")
	print("6)Mostrar Alumno con la nota mas alta")
	print("7)Mostrar la nota promedio de los alumnos")
	print("8)Salir\n")
	
def ejecutar(py):
	os.system("cls")
	py["run_cmd"]("h Instituto",py)
	opt=""
	while (opt != "8"):
		py["run_cmd"]("f -d",py)
		if (opt == "1"):
			py["run_cmd"]("i",py)
		elif (opt == "2"):
			py["run_cmd"]("f Nota>6.5",py)
			py["run_cmd"]("v",py)
		elif (opt == "3"):
			py["run_cmd"]("f Nota>6.5",py)
			py["run_cmd"]("c",py)
		elif (opt == "4"):
			materia = input("Materia: ")
			py["run_cmd"]("f Materia="+materia,py)
			py["run_cmd"]("v",py)
		elif (opt == "5"):
			alumno = input("Materia: ")
			py["run_cmd"]("f Alumno="+alumno,py)
			if(len(py["selec"])>0):
				print("Si, esta matriculado en al menos una materia")
			else:
				print("No, no tiene ninguna materia asignada")
		elif (opt == "6"):
			py["run_cmd"]("max Nota",py)
			py["run_cmd"]("v",py)
		elif (opt == "7"):
			py["run_cmd"]("p Nota",py)
		else:
			menu()
		opt = input("> ")
		
def instalar():
	app = {"leer": leer, "ayuda":menu, "ejecutar":ejecutar}		
	return app

