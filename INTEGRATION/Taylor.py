import numpy as np
import matplotlib.pyplot as plt
# SUM OF SINES
def sinesum(t, b, N):
    S = np.zeros_like(t, dtype=float)
    for i in range(1, N+1):
        S += b[i-1] * np.sin(i*t)
    return S
# VERIFICATION TEST
def test_sinesum():
    t = np.array([-np.pi/2, np.pi/4])
    N = 2
    b = np.array([4, -3])
    S = sinesum(t, b, N)
    print(S)
#FUNCTION
def f(t):
    return np.sin(t)
#PLOT FOR COMPARISON ON THE APPROXIMATION
def plot_compare(f, N, M):
    b = np.linspace(0, 1, N)   # coefficients
    t = np.linspace(-np.pi, np.pi, M)
    S = sinesum(t, b, N)
    
    plt.figure(figsize=((10, 5)))
    plt.plot(t, f(t), "r-", label="f(t)")
    plt.plot(t, S, "b--", label="S_N(t)")
    plt.legend()
    plt.grid()
    plt.show()

test_sinesum()
plot_compare(f, N=5, M=1000)
