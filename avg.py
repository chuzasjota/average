# Initialize the matrix to save each student's name and notes
M = []
estudiantes = 2
notas = 6

for i in range(estudiantes):
    nombre = input('Nombre del estudiante: ')
    notas_estudiante = [nombre]
    for j in range(notas):
        nota = input('Ingrese la nota #%d: '%(j+1))
        notas_estudiante.append(float(nota))
    M.append(notas_estudiante)

# You can now iterate throug M and get, let's say, each students average grade
# Or the grade x mean.
# Example:
# Print each student average grade

def get_mean(numbers):
    return sum(numbers) / max(len(numbers), 1)

for student in M:
    name = student[0]
    # To get the grades, ignore the first item (name of the student) ***
    grades = student[1:]
    avg = get_mean(grades)
    print('Notas de %s: %s'%(name, grades))
    print('Nota promedio de %s: %d\n'%(name, avg))
    # If you're using python 3.6+, you can use f-strings (another awesome feature introduced in python 3.6), 
    # just like this: print(f'Notas de {name}: {grades}')


# ***    
# Python list slicing is awesome!, learn more: https://stackoverflow.com/a/509295/2850557
# in spanish: http://librosweb.es/foro/pregunta/250/como-entender-bien-la-notacion-slice-de-python/