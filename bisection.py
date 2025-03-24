import numpy as np  
def compute_function(a,coefficients) :
    result = 0.0
    degree = len(coefficients) - 1
    for i in range(degree) :
        result = result  + pow(a, degree -i ) * coefficients[i]
        return result

def bisectionMethon(a,b, coefficients):
    f_b = np.polyval(coefficients,b)
    f_a = np.polyval(coefficients,a)
    if f_b * f_a > 0 :
        return
    else :
        error = pow(10,-5)
        while abs(b- a) > error:
            c = (a + b) / 2 
            f_c = np.polyval(coefficients,c)
            
            if(f_c == 0):
                return c
            elif (f_c * f_a < 0):
                b = c
            else:
                 a = c
    return  (a + b) / 2 
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
    result = bisectionMethon(a,b,function_factor)
    print(result)
 
    if result is not None:
        print(f"Approximate root: {result}")
    else:
        print("Bisection method failed.")

if __name__ == "__main__":
    main()
        