## CLASES ##

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson()) #puede llamar a la clase con paréntesis o sin paréntesis 

"""
class Person:
    def __init__(self, name, surname): #sirve para crear un constructor de clase 
        self.name = name
        self.surname = surname

my_person = Person('Sara', 'Gonzalez')
#print(my_person.name)
print(f"{my_person.name} {my_person.surname}")

----------------------------------------------------------------
class Person:
    def __init__(self, name, surname): #sirve para crear un constructor de clase 
        self.full_name = f"{name} {surname}"
    def walk (self): #podemos definir una funcion dentro de una clase con sus respectivas regals y palabra self apra poder utilizar los argumentos de la clase
        print(f"{self.full_name} está caminando")

my_person = Person('Sara', 'Gonzalez')
#print(my_person.full_name)
my_person.walk()

"""
class Person:
    def __init__(self, name, surname, alias ="Sin alias"): #se puede pasar un alias por defecto  
        self.full_name = f"{name} {surname} ({alias})"
    def walk (self): #podemos definir una funcion dentro de una clase con sus respectivas regals y palabra self apra poder utilizar los argumentos de la clase
        print(f"{self.full_name} está caminando")

my_person = Person('Sara', 'Gonzalez')
#print(my_person.full_name)
my_person.walk()
my_other_person = Person("Sara", "Gonzalez", "SG")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)
