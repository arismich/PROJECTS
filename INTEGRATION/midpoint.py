def midpoint(f, a, b, n):
    h = (b-a) / n
    f_sum = 0
    for i in range(0, n, 1):
        x = (a + h/2.0) + i*h
        f_sum = f_sum + f(x)
        
    return h*f_sum
