import numpy as np
import random

from sympy import *
def newton_method(cofficent, inital_guess = None, error_rate = 1e-6, max_iteration = 1000000):
    x = Symbol('x')
    degree = len(cofficent)-1
    polynomial_function = sum((x**(degree - i)) * cofficent[i] for i in range(degree))

    if(inital_guess == None) :
        current_guess = random.uniform(-10,10)
    else :
        current_guess = inital_guess   
    yprime = polynomial_function.diff(x)
    f_prime = lambdify(x, yprime, 'numpy') 
    for i in range(max_iteration):
        f_value = np.polyval(cofficent,current_guess)
        f_prime_value = f_prime(current_guess)
        if(f_prime_value == 0) :
            current_guess =  random.uniform( -10 , 10)
            power_of_boundary += 1
            continue
        new_guess = current_guess - (f_value /f_prime_value)
        if(abs(np.polyval(cofficent,new_guess)) < error_rate):
            break
        current_guess = new_guess
        
    return current_guess       
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
        