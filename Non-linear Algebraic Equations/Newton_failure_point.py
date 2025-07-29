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


def Tangent_Plotting(ax, x_vals, title):
    t = np.linspace(-2, 2, 400)  # domain for function
    ax.plot(t, f(t), 'b-', label='tanh(x)')  # plot function
    for x in x_vals:
        x_local = np.linspace(x - 0.5, x + 0.5) 
        y_local = dfdx(x)*(x_local - x) + f(x)
        ax.plot(x_local, y_local, "r--")
        ax.scatter([x], [f(x)], color='black')  # Newton points
        
    ax.axhline(0, color='k', linewidth=0.8)
    ax.set_title(title)
    ax.legend()
    ax.grid()

#IF USED X=1.09 THE NEWTON METHOD FAILS !!
_, _, x_vals1 = Newton(f, dfdx, x=1.08, eps=1e-6)
_, _, x_vals2 = Newton(f, dfdx, x=1.09, eps=1e-6)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

Tangent_Plotting(axes[0], x_vals1, "Newton starting at x0=1.08 (Converges)")
Tangent_Plotting(axes[1], x_vals2, "Newton starting at x0=1.09 (Fails)")
plt.show()