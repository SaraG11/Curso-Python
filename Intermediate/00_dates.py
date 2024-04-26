## DATES ##
#import datetime #es del sistema la palabra reservada para trabajar con fechas 

from datetime import datetime # de esta manera se importan modulos de cierto datos 

#definir
now = datetime.now() #esta es una funcion que se tiene dentro de datetime de este momento 

"""
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
"""

timestamp = now.timestamp()
print(timestamp)

#trabajar con una fecha en específico 
year_2025 = datetime(2025, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)