from midpoint import midpoint

def midpoint_test():
    n = 2
    f = lambda x: 2 * (x)**3
    F = lambda x: 0.5 * (x)**4
    numerical = midpoint(f, 1, 3, n)
    expected = F(3) - F(1)
    error = abs(numerical-expected)
    print("n={:d}: {:.4f}, error: {:g}".format(n, numerical, error))
    
if __name__ == "__main__":
    midpoint_test()