## FUNCIONES ##

## Palabra reservada para funciones en python es *def* ##

def my_function (): ##definimos una funcion
    print("Esto es una funcion")

# llama a la funcion
my_function ()

def sum_two_values (first_value, second_value):
    print(first_value + second_value)

sum_two_values (5, 8)
sum_two_values (10, 8)
sum_two_values ('Sara', 'Gonzalez')

# Función con parámetros de entrada/argumentos y retorno

def sum_values_return (first_value, second_value):
    #print(first_value + second_value)
    my_sum = first_value + second_value
    return my_sum

my_result = sum_values_return(10,5)
print(my_result)

# Función con parámetros de entrada/argumentos por clave

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Gonzalez", name = "Sara")

# Función con parámetros de entrada/argumentos por defecto

def print_name_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_default("Gonzalez", "Sara", "SG")

# Función con parámetros de entrada/argumentos arbitrarios

def print_txt(*texts):
    for text in texts:
        print(text.upper())


print_txt("Hola", "Python", "MoureDev")
print_txt("Hola")