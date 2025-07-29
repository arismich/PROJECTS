import sys

def Newton(f, dfdx, x, eps):
    f_value = f(x)
    iteration_counter = 0
    while abs(f_value) > eps and iteration_counter < 100:
        try:
            x = x - f_value/dfdx(x)
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", x)
            sys.exit(1)
        
        f_value = f(x)
        iteration_counter = iteration_counter + 1
        
    if abs(f_value) > eps:
        iteration_counter = -1
            
    return x, iteration_counter

if __name__ == "__main__":
    def f(x):
        return x**2 - 9
    
    def dfdx(x):
        return x*2
        
    solution, no_iterations = Newton(f, dfdx, x=1000, eps=1.0e-6)
    
    if no_iterations > 0:
        print("Number of function calls: {:d}".format(1+2*no_iterations))
        print("A solution is: {:f}".format(solution))
    else:
        print("Solution not found!")