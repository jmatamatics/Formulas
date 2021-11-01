import math

def c_area():
                r = int(input("Enter the raduis: "))
                A = math.pi * r**2
                print(f'a = pi * r^2 \n'
                      f'a = pi * {r}^2 \n'
                      f'The area of the circle is {A:.3f}')


def circumference():
                d = int(input("Enter the diameter: "))
                A = 3.14*d
                print(f'A = pi * d \n'
                      f'A = pi *{d} \n'
                      f'The circumference is {A:.3f}')


def radians_to_degrees():
                    r = int(input("Enter the amount of radians: "))
                    d = r*180/math.pi
                    print(f'd = (r * 180)/pi \n' 
                          f'd = ({r} * 180)/pi \n'
                          f"{r} radians equals {d:.3f} degrees")


def degrees_to_radians():
                    d = int(input("Enter the amount of degrees: "))
                    r = d*math.pi/180
                    print(f'r = (d * pi)/180 \n'
                          f'r = ({d} * pi)/180 \n'
                          f"{d} degrees equals {r:.3f} degrees")