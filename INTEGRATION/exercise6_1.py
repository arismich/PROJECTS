def gp(msg="Quick update"):
    import os
    os.system('git add .')
    os.system(f'git commit -m "{msg}"')
    os.system('git push')
    
from trapezoidal import trapezoidal

def trapezoidal_test():
    n = 2
    f = lambda x: 2 * (x)**3
    F = lambda x: 0.5 * (x)**4
    
    expected = F(3) - F(1)
    numerical = trapezoidal(f, 1, 3, n)
    error = abs(expected - numerical)
    print("n={:d}: {:.4f}, error: {:g}".format(n, numerical, error))

if __name__ == "__main__":
    trapezoidal_test()
    
