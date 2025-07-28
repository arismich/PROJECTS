# PRODUCT OF SINE FUNCTIONS
from midpoint import midpoint
import numpy as np

def sine_product(a, b, j, k):
    n = 1000

    f = lambda x: np.sin(j*x) * np.sin(k*x)
    
    Product = midpoint(f, a, b, n)

    x = np.linspace(-np.pi, np.pi, 1000)

    plt.plot(x, np.sin(j*x) * np.sin(k*x))
    plt.title(f"∫ sin({j}x)sin({k}x) dx ≈ {Product:.4f}")
    plt.show()
    
sine_product(-np.pi, np.pi, j=1, k=1)

def sine_product(a, b):
    n = 1000

    
    products = []
    for j in range(1, 11, 1):
        for k in range(1, 11, 1):
            f = lambda x, j=j, k=k: np.sin(j*x) * np.sin(k*x)
            p = trapezoidal(f, a, b, n)
            products.append(p)
    print(products)
    return products




    

