## Tuples, conjunto de valores inmutables, elementos que ya se tienen guardados  ##

#definir una tupla, con su palabra resrvada tuple
my_tuple = tuple()
my_other_tuple = () #2da forma de definir una tupla

my_tuple = (25, 1.53, "Sara", "Gonzalez", "Sara")
my_other_tuple = (60, 30, 35)

print(my_tuple)
print(type(my_tuple))

#print(my_tuple[0])
#print(my_tuple[-1])

print(my_tuple.count("Sara"))
print(my_tuple.index("Gonzalez")) #indica el índice que es en 3
print(my_tuple.count("Sara"))

#my_tuple[1] = 1.60 # ERROR , no se puede asignar 
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6]) #buscar los lementos entre el 3 y el 6 


#borrar, borra la variable. 
del my_tuple
print(my_tuple) # es un error, NameError: name 'my_tuple' is not defined