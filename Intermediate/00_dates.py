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

'''
def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
'''

from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today() #se puede tomar el día de ahora en curso

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6) #pero al igual se pueden pasar los parámetros de la fecha 
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks= 10)

end_timedelta = timedelta(300, 100, 100, weeks= 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
