import sympy as sym
import matplotlib.pyplot as plt

x = sym.symbols("x")
f_expr = sym.tanh(x)
dfdx_expr = sym.diff(sym.tanh(x))

f = sym.lambdify([x], f_expr)
dfdx = sym.lambdify([x], dfdx_expr)


def Newton(f, dfdx, x, eps):
    f_value = f(x)
    iteration_counter = 0
    x_values = []

    while abs(f_value) > eps and iteration_counter < 100:
        try:
            x = x - f_value/dfdx(x)
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", x)
            sys.exit(1)
            
        f_value = f(x)
        iteration_counter = iteration_counter + 1
        
        x_values.append(x)
        
    if abs(f_value) > eps:
        iteration_counter = -1
            
    return x, iteration_counter, x_values


solution, no_iterations, x_vals = Newton(f, dfdx, x=1.08, eps=1.0e-6)


def Tangent_Plotting(x_vals):
    t = np.linspace(-2, 2, 400)  # domain for function
    plt.plot(t, f(t), 'b-', label='tanh(x)')  # plot function
    for x in x_vals:
        x_local = np.linspace(x - 0.5, x + 0.5) 
        y_local = dfdx(x)*(x_local - x) + f(x)
        plt.plot(x_local, y_local, "r--")
        plt.scatter([x], [f(x)], color='black')  # Newton points
        
    plt.axhline(0, color='k', linewidth=0.8)
    plt.title("Newton iterations with tangents")
    plt.legend()
    plt.grid()
    plt.show()
Tangent_Plotting(x_vals)