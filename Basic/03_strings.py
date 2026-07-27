##STRINGS##
'''
my_string = 'Mi String'
my_other_string = 'Mi otro String'

print(len(my_string)) Hallar la longuitud
print(len(my_other_string))

print(my_string + " "+ my_other_string) Concatenacion

my_new_line_string = "Este es un String \ncon salto de linea"
print(my_new_line_string)

my_tab_string = '\tEste un string con tabulacion'
print(my_tab_string)


my_scape_string = '\\tEste un string \n escapado'
print(my_scape_string)
'''
#FORMATEO#
'''
name, surname, age= 'Sara','Gonzalez', 25
print('Mi nombre es {} {} y mi edad es {}'.format(name,surname,age))
print('Mi nombre es %s %s y mi edad es %s' %(name,surname,age))
print('Mi nombre es ' + name + '' + surname + 'y mi edad es ' + str(age))

#inferencia#
print(f'Mi nombre es {name} {surname} y mi edad es {age}') # tipo de formateo se refiere la f
'''
#desmpaquetado de caracteres#
language ="python"
a, b, c, d, e, f= language
# print(a)
# print(b)

# Divisón
language_slice = language[1:3] #Cuenta las letras que hay entre el 1 y el 3 sin contar el 3
# print(language_slice)

# Reverse
reversed_languaje= language[::-1] #muestra el contenido de la variable al reves
# print(reversed_languaje)

# Funciones
# print(language.capitalize()) #pone la primera letra en mayuscula
# print(language.upper()) #todo en mayusculas
# print(language.count('t'))  #cuaenta cuantas veces aparece la letra 't'
# print(language.isnumeric()) #verifica si la cadena es un numero
# print('1'.isnumeric()) #verifica si la cadena es un numero
# print(language.lower()) #todo en minusculas
# print(language.upper().isupper()) #verifica si la cadena esta en mayusculas

print(language.startswith('py')) #comprueba si la cadena empieza con 'py'
print('Py' == 'py') 