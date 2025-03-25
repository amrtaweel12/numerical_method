import numpy as np
import random

from sympy import *
def newton_method(cofficent):
    intial_value = random.random() * 10
    x = Symbol('x')
    degree = len(cofficent)
    y = x
    for i in range(degree):
        y = y + (x** (degree - i)) * cofficent[i]
    y = y -x
    yprime = y.diff(x)
    fprime = lambdify(x, yprime, 'numpy')
    f_intial = np.polyval(cofficent, intial_value)
    while f_intial > pow(10,-6):
        intial_value = intial_value - (f_intial/fprime(intial_value))
        f_intial =  np.polyval(cofficent, intial_value)
    return intial_value       
def main():
    cofficent =[]
    while(True) :
        user_input = input("Enter something (enter q to exit): ")
        if(user_input == 'q') :
            break
        else:
            cofficent.append(float(user_input))
    result = newton_method(cofficent)
    print(result)

if __name__ == "__main__":
    main()
        