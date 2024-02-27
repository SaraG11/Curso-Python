## LISTAS conjunto de datos ##

#nombre   declaracion objeto, el tipo de dato es lista
#my_list = list()

#también es una lista
my_other_list = []


#forma de agrupar datos, en orden, siguiendo una lista
my_list = [25, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

#no hace falta que guardemos el mismo tipo de dato 
my_other_list = [35, 1.52, 'Sara G', 'Gonzalez']

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[3])
print(my_other_list.count('Gonzalez')) 
print(my_list.count(30))  #retorna el numero de valor, cuantas veces se repite

#desempaquetar
#age, height, name = my_other_list ---- ERROR NECESITA TODOS LOS ELEMENTOS DE LA LISTA
age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list)

#tipos dinamicos
my_list = 'Hola Py'
print(my_list)

my_list = ['Hola Py']
print(my_list)
print(type(my_list))

