## CHALLENGES ##

'''
FIZZ BUZZ

Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

#creacion de funcion
def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index %5 == 0:
            print('FizzBuzz')
        elif index % 3 == 0:
            print('Fizz')
        elif index % 5 == 0:
            print('Buzz')
        else:
            print(index)

fizzbuzz()
'''

'''
 Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
    - Un Anagrama consiste en formar una palabra reordenando TODAS
      las letras de otra palabra inicial.
    - NO hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.
'''

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return word_one == word_two


print(is_anagram('Amor', 'Roma'))