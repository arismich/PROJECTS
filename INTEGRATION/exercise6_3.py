#SOLVING AN INTEGRAL USING MIDPOINT AND TRAPEZOIDAL METHODS

# imports
from midpoint import midpoint
from trapezoidal import trapezoidal
# definition of a function using midpoint methodology:
def mp(a, b):
    """
    Definition of a midpoint methodology function for the given integral
    x(x-1) from 2 to 6
    """
    f = lambda x: (x)**2 - (x) # function
    F = lambda x: (1/3) * (x)**3 - 0.5 * (x)**2 # anti-derivative
    
    numerical_2 = midpoint(f, a, b, n=2) # 2 iterations
    numerical_100 = midpoint(f, a, b, n=100) # 100 iterations
    expected = F(b) - F(a)
    
    error_2 = abs(numerical_2 - expected)
    error_100 = abs(numerical_100 - expected)
    
    print("n= {:d}: {:.4f}, error = {:g}".format(2, numerical_2, error_2))
    print("n= {:d}: {:.4f}, error = {:g}".format(100, numerical_100, error_100))
    return numerical_100, error_100

    

def tz(a, b):
    """
    Definition of a trapezoidal methodology function
    x(x-1) from 2 to 6

    """
    
    f = lambda x: (x)**2 - (x) # function
    F = lambda x: (1/3) * (x)**3 - 0.5 * (x)**2 # anti-derivative
    
    numerical_2 = trapezoidal(f, a, b, n=2) # 2 iterations
    numerical_100 = trapezoidal(f, a, b, n=100) # 100 iterations
    expected = F(b) - F(a)
    
    error_2 = abs(numerical_2 - expected)
    error_100 = abs(numerical_100 - expected)

    print("n= {:d}: {:.4f}, error = {:g}".format(2, numerical_2, error_2))
    print("n= {:d}: {:.4f}, error = {:g}".format(100, numerical_100, error_100))
    return numerical_100, error_100


print(mp(2, 6))
print("="*10)
print(tz(2, 6))
