# We consider integrating the sine function sin(x) from zero to b

# imports
from midpoint import midpoint
from trapezoidal import trapezoidal
import numpy as np
# definition of a function using midpoint methodology:
def mp(a, b):
    """
    Definition of a midpoint methodology function for the given integral
    sin(x) from a to b
    """
    f = lambda x: np.sin(x) # function
    F = lambda x: -np.cos(x) # anti-derivative
    n = 2 # iterations
    numerical = midpoint(f, a, b, n)
    expected = F(b) - F(a)
    
    error = abs(numerical - expected)
    
    print("Midpoint method:\nn= {:d}: {:.4f}, error = {:g}".format(2, numerical, error))
    return numerical, error
    

def tz(a, b):
    """
    Definition of a trapezoidal methodology function
    x(x-1) from 2 to 6

    """
    n = 2 # iterations

    f = lambda x: np.sin(x) # function
    F = lambda x: -np.cos(x) # anti-derivative
    
    numerical = trapezoidal(f, a, b, n=2)
    expected = F(b) - F(a)
    
    error = abs(numerical - expected)

    print("Trapezoidal method:\nn= {:d}: {:.4f}, error = {:g}".format(2, numerical, error))
    return numerical, error


print(mp(0, np.pi))
print("="*40)
print(tz(0, np.pi))

