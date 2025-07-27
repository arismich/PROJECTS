def trapezoidal(f, a, b, n):
    h = (b-a) / n
    f_sum = 0
    for i in range(1, n, 1):
        x = a + i*h
        f_sum = f_sum + f(x)
        
    return h*(0.5*f(a) + f_sum + 0.5*f(b))


if __name__ == "__main__":
    n = 2 
    f = lambda x: 2 * (x)**3
    numerical = trapezoidal(f, 1, 3, n)
    print(numerical)  