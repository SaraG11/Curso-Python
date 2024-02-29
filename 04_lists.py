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
"""
#age, height, name = my_other_list ---- ERROR NECESITA TODOS LOS ELEMENTOS DE LA LISTA
age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list)

"""

#elementos de la lista 
"""
my_other_list.append("SG") #un append lo va insertar la final de una lista
print(my_other_list)

my_other_list.insert(1, "NARANJA") #en que posicion quiere que insertemos el valor
print(my_other_list)

my_other_list.remove("NARANJA") #elimina un valor que se desea
print(my_other_list)

my_list.remove(30) #elimina el primer valor aunque haya dos 
print(my_list)
"""

#estructuras colas
my_list.pop() #elimina el ultimo registro o desapila la lista 
print(my_list.pop())


my_pop_element = my_list.pop(2)
print(my_pop_element)
# print(my_list.pop(2)) el numero del elemento que se quiere desapilar recordando que la lista inicia con 0

#eliminacion de un valor de la lista sin guardarlo por indice 
del my_list[2]
print(my_list)

#copiar una lista
my_new_list = my_list.copy()

my_list.clear() #no habrá ningun elemento de la lista
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort() #ordena, criterios para ordenar de mayor a menor
print(my_new_list)

# sublistas
print(my_new_list)



my_other_list.insert(1, "NARANJA") #en que posicion quiere que insertemos el valor
print(my_other_list)

my_other_list[1] = 'Rojo'
print(my_other_list)
"""
#tipos dinamicos
my_list = 'Hola Py'
print(my_list)

my_list = ['Hola Py'] #esto ya es una lista con poner los corchetes
print(my_list)
print(type(my_list))
"""


