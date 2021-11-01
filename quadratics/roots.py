
import math 

def roots():
    a = int(input('For your ax**2 + bx + c equation, enter a:'))
    b = int(input('enter b:'))
    c = int(input('enter c:'))
    
    if b**2 -4 * a * c >= 0:
        root1, root2 = (-b - math.sqrt(b**2 -4 * a * c))/(2 * a), (-b + math.sqrt(b**2 -4 * a * c))/(2 * a)
        print(f'For your ax^2 + bx + c equation, the roots are {root1: .2f} and {root2: .2f}.')  
    else:
        i1, i2 = math.sqrt(abs(b**2 - 4 * a * c)), math.sqrt(abs(b**2 - 4 * a * c))
        b_ = -b
        d = 2 * a
        print(f'For your ax^2 + bx + c equation, the roots are ({b_} -{i1: .2f}i)/{d} and ({b_} +{i1: .2f}i)/{d}.') 
