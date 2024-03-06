## DICCIONARIOS ##
#Estructura de datos que sirve para almacenar clave-valor

my_dict = dict() #Manera de declaarar un diccionario
my_other_dict = {}

my_other_dict = {"Nombre": "Sara",
                 "Apellido": "Gonzalez", "Edad": 25, 1: "Python"}

my_dict = {
        "Nombre": "Sara",
        "Appelido": "Gonzalez",
        "Edad": 25,
        "Lenguaje": {"Python", "Swift", "Kotlin"},  
        1: 1.52     
    }

print(my_other_dict)
print(my_dict)

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

#Agragr un elemento a un diccionario
my_dict["Calle"] = "Calle 1"
print(my_dict)

#El del era para eliminar todo un conjunto de elementos, pero si le asignamos un elemento en específico como es Calle es la manera para eliminar uno del diccionario 
del my_dict["Calle"]
print(my_dict)

#buscando por clave, no por valor
print("Nombre" in my_dict) #true

#
print(my_dict.items()) #tenemos un listado de cada uno de las items
print(my_dict.keys()) #Las claves de los diccionarios
print(my_dict.values())# Los valores de las claves de los diccionarios
print(my_dict.fromkeys())

