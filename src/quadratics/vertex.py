import math

def vertex():
    a = int(input('For your ax**2 + bx + c equation, enter a:'))
    b = int(input('enter b:'))
    c = int(input('enter c:'))
    V = (-b/(2 * a), -(b**2 - 4 * a * c)/(4* a))
    print(f'V = (-b/(2 * a), -(b^2 - 4 * a * c)/(4 * a)) \n'
          f'V = (-{b}/(2 * {a}), -({b}^2 - 4 * {a} * {c})/(4 * {a})) \n'
          f'The vertex is {V}')


