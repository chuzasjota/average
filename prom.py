# Yorledy Gonzales - Fundamentos de programación

#variable usu --> nombre de usuario
usu = "dfp"
#variable usu --> nombre de usuario
password = "1234"
#Se le pide al usuario ingresar en la aplicacion
print("Login Plataforma de notas")
#Se guarda en la variable usuP y passwordP lo ingresado por el usuario
usuP= input("ingrese usuario\n")
passwordP = input("ingrese contraseña\n")

#Se hace la validación de que estos datos sean iguales
#Si son iguales ingresa al sistema sino se imprime mensaje "Datos incorrectos"
if ((usu == usuP) & (password == passwordP)):
	#Mensaje de bienvenida para el docente
	print("Bienvenido Docente Diego Fernando Pescador")
	print("Periodo lectivo: 2018-1")
	print("Asignaturas a cargo:\n")
	print("Fundamentos de programacion - Grupo 409 - Código 1")
	print("Fundamentos de programacion - Grupo 418 - Código 2")
	print("Estructuras - Grupo 61 - Código 3")

	#Se le pide al usuario la asignatura a calificar
	asignatura = int(input("Ingrese el codigo de la asignatura\n"))
	#Se valida la asignatura elegida por el usuario
	if asignatura == 1:
		#variable estudiantes --> total de estudiantes de la asignatura
		estudiantes = 3
		#estCont --> contador de estudiantes
		estCont = 0
		#totalNotas --> Total de notas de la asignatura
		totalNotas = 4
		#suma --> se guardara la suma de las notas
		suma = 0
		asig1List = []
		
		#ciclo mientras para ingresar las notas de los estudiantes
		for e in range(estudiantes):
			#nomEstu --> Nombre del estudiante
			nomEstu = input("Nombre del estudiante\n")
			asig1List.append(nomEstu)
			#ciclo for para ingresar las notas del estudiante
			for i in range(totalNotas):
				#Ingresamos las notas
				print("Ingrese la nota ", i+1)
				nota = input()
				nota = float(nota)
				#suma --> guarda la sumatoria de las notas
				suma = suma + nota
				asig1List.append(nota)
			#promedio --> guarda el resultado del promedio, ademas redondeamos el decimal a uno
			promedio = round((suma / totalNotas), 1)
			#Se guarda el promedio tambien en la lista
			asig1List.append(promedio)
			#mensajes sobre 
			print("Promedio : " + str(promedio))
			print("Lista Actualizada : ", asig1List)
	elif asignatura == 2:
		#variable estudiantes --> total de estudiantes de la asignatura
		estudiantes = 3
		#estCont --> contador de estudiantes
		estCont = 0
		#totalNotas --> Total de notas de la asignatura
		totalNotas = 4
		#suma --> se guardara la suma de las notas
		suma = 0
		asig2List = []
		
		#ciclo mientras para ingresar las notas de los estudiantes
		while(estCont < estudiantes):
			#nomEstu --> Nombre del estudiante
			nomEstu = input("Nombre del estudiante\n")
			asig2List.append(nomEstu)
			#ciclo for para ingresar las notas del estudiante
			for i in range(totalNotas):
				#Ingresamos las notas
				print("Ingrese la nota ", i+1)
				nota = input()
				nota = float(nota)
				#suma --> guarda la sumatoria de las notas
				suma = suma + nota
				asig2List.append(nota)
			#promedio --> guarda el resultado del promedio, ademas redondeamos el decimal a uno
			promedio = round((suma / totalNotas), 1)
			#Se guarda el promedio tambien en la lista
			asig2List.append(promedio)
			#mensajes sobre 
			print("Promedio : " + str(promedio))
			print("Lista Actualizada : ", asig2List)
			#se suma el contador del estudiante
			estCont += 1
	elif asignatura == 3:
		#variable estudiantes --> total de estudiantes de la asignatura
		estudiantes = 3
		#estCont --> contador de estudiantes
		estCont = 0
		#totalNotas --> Total de notas de la asignatura
		totalNotas = 4
		#suma --> se guardara la suma de las notas
		suma = 0

		asig3List = []
		#ciclo mientras para ingresar las notas de los estudiantes
		while(estCont < estudiantes):
			#nomEstu --> Nombre del estudiante
			nomEstu = input("Nombre del estudiante\n")
			asig3List.append(nomEstu)
			#ciclo for para ingresar las notas del estudiante
			for i in range(totalNotas):
				#Ingresamos las notas
				print("Ingrese la nota ", i+1)
				nota = input()
				nota = float(nota)
				#suma --> guarda la sumatoria de las notas
				suma = suma + nota
				asig3List.append(nota)
			#promedio --> guarda el resultado del promedio, ademas redondeamos el decimal a uno
			promedio = round((suma / totalNotas), 1)
			#Se guarda el promedio tambien en la lista
			asig3List.append(promedio)
			#mensajes sobre 
			print("Promedio : " + str(promedio))
			print("Lista Actualizada : ", asig3List)
			#se suma el contador del estudiante
			estCont += 1
else:
	print("Datos incorrectos")