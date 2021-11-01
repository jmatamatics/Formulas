import math

def prism_v():
    B = int(input("Enter the base area: "))
    h = int(input("Enter the height: "))
    V = B * h
    print(f'V = B * h \n'
          f'V = {B} * {h} \n'
          f'The prism volume equals{V: .2f}')    



def cylinder_v():
    r = int(input("Enter the raduis: "))
    h = int(input("Enter the height: "))
    V = math.pi * r**2 * h
    print(f'V = pi * r^2 * h \n'
          f'V = pi * {r}^2 * {h} \n' 
          f'The cylinder volume equals{V: .2f}')  



def cone_v():
    r = int(input("Enter the raduis: "))
    h = int(input("Enter the height: "))
    V = (math.pi * r**2 * h)/3
    print(f'V = (pi * r^2 * h)/3 \n' 
          f'V = (pi * {r}^2 * {h})/3 \n'
          f'The cone volume equals{V: .2f}') 


def sphere_v():
    r = int(input("Enter the raduis: "))
    V = (math.pi * r**2 * 4)/3
    print(f'V = (pi * r^2 * 4)/3 \n'
          f'V = (pi * {r}^2 * 4)/3 \n'
          f'The sphere volume equals{V: .2f}') 