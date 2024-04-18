## Loops (Bucles, ciclos) ##

#While (mientras sea verdadero haz algo)
"""
my_condition = 0

while my_condition < 10:
    print(my_condition) 
    my_condition += 2 #incremento
else: #es opcional
    print("Mi condicion es mayor o igual a 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1 
    if my_condition == 15:
        print("Se detiene la ejecución")
        break

    print(my_condition)

print("La ejecucion continúa")
"""

# For 

my_list = [25, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (25, 1.53, "Sara", "Gonzalez", "Sara")

for element in my_tuple:
    print(element)

my_set = {"Sara", "Gonzalez", 25}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Sara", "Apellido": "Gonzalez", "Edad": 25, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario ha finalizado")


for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario ha finalizado")