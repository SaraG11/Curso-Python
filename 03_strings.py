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
print(f'Mi nombre es {name} {surname} y mi edad es {age}')
'''
#desmpaquetado de caracteres#
language ="python"
a, b, c, d, e, f= language
print(a)
print(b)

# Divisón
language_slice = language[1:3]
print(language_slice)

# Reverse
#reversed_languaje= language[::-1]
#print(reversed_languaje)

# Funciones
print(language.capitalize()) 
print(language.upper()) 
print(language.count('t')) 
print(language.isnumeric()) 
print('1'.isnumeric()) 
print(language.lower()) 
print(language.upper().isupper()) 

print(language.startswith('py')) 
print('Py' == 'py') 