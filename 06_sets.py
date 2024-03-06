## SETS ##

my_set = set() #declaracion de un set. Set es un tipo de dato
my_other_set = {}

#print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Sara", "Gonzalez", 25}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add ("SaraG") 
print(my_other_set) #Un set no es una estructura ordenada

my_other_set.add ("SaraG") # Un set no admite repetidos
print(my_other_set) 

print("Gonzalez" in my_other_set) #true. Verifica si un elemento se encuentra en el set
print("sara" in my_other_set) #false 

my_other_set.remove("Gonzalez")
print(my_other_set)

my_other_set.clear() #elimina todos los elementos
print(len(my_other_set))

del my_other_set
#print(my_other_set) # error ya que se ha eliminaod definitivamente 

#No es reocmendable transofrmar el objeto de set a una lista porque varia el orden y si se quiere tomar un objeto de la lista este cambiaría
my_set = {"Sara", "Gonzalez", 25}
my_list = list(my_set)
print(my_list)
print(my_list[0])


#Unir dos set
my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
#print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) #no se duplica la union que ya existe pero si se agrega lo que no existe

#diferencia
print(my_new_set.difference(my_set)) #se quitan los elementos que tiene la diferencia
