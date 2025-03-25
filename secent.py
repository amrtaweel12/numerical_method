import numpy as np

def secant_method(a,b, coefficent, error_rate = 1e-6,max_iteration = 100000):
    for  __ in range(max_iteration):
        f_a= np.polyval(coefficent,a)
        f_b= np.polyval(coefficent,b)
        new_guess = b - f_b * (b - a) / (f_b - f_a)
        a, b = b, new_guess
        x = np.polyval(coefficent, b)
        if abs(np.polyval(coefficent, b)) < error_rate:
            break
    return b    
def main():
    function_factor =[]
    a = float(input("a: "))                   
    b = float(input("b: "))
    while(True) :
        user_input = input("Enter something (enter q to exit): ")
        if(user_input == 'q') :
            break
        else:
            function_factor.append(float(user_input))
    result = secant_method(a,b,function_factor)
    print(result)
 
    if result is not None:
        print(f"Approximate root: {result}")
    else:
        print("Bisection method failed.")

if __name__ == "__main__":
    main()
        