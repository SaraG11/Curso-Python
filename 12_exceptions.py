## Excepciones manejo de errores ##

numberOne, numberTwo = 5, 1
numberTwo = '1'

# esto es un error controlado, a mano, sabiendo que puede pasar 
#if type(numberTwo) == int:
#    print(numberOne + numberTwo) 
#else:
#    print("no se cumplió")

#Try except
try:
    print(numberOne + numberTwo) 
    print("No se ha producido un error")
except:
    #se ejecuta si se produce una excepcion 
    print("Se ha producido un error")

#Try except else
try:
    print(numberOne + numberTwo) 
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    #se ejecuta si no se produce una excepcion 
    print("La ejecucion continúa correctamente")

#Try except else finally
try:
    print(numberOne + numberTwo) 
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    #se ejecuta si no se produce una excepcion 
    print("La ejecucion continúa correctamente")
finally:
    #se ejecuta siempre
    print("La ejecucion continúa")

# Excepciones por tipo
try:
    print(numberOne + numberTwo) 
    print("No se ha producido un error")
except TypeError: #tipo de error, solo si se produce este tipo de error
    #se ejecuta si se produce una excepcion 
    print("Se ha producido un TypeError")
except ValueError: #tipo de error, solo si se produce este tipo de error
    #se ejecuta si se produce una excepcion 
    print("Se ha producido un ValueError")

# Captura de la informacion de la excepcion 
try:
    print(numberOne + numberTwo) 
    print("No se ha producido un error")
except TypeError as error: 
    print(error)
except Exception as exception: #excepcion genérica
    print(exception)

