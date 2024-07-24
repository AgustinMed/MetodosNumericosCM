import sympy as sp

def secant_method(f_expr, p0, p1, n_iterations):
    f = sp.lambdify(x, f_expr)
    
    pn_values = [p0, p1]
    
    # Método de la secante
    for n in range(n_iterations):
        p_n_minus_1 = pn_values[-1]
        p_n_minus_2 = pn_values[-2]
        
        # Calculo pn usando la fórmula de la secante
        p_n = p_n_minus_1 - (f(p_n_minus_1) * (p_n_minus_1 - p_n_minus_2)) / (f(p_n_minus_1) - f(p_n_minus_2))
        
        # Guardo el nuevo valor de pn
        pn_values.append(p_n)
    
    return pn_values

expr_input = input("Introduce la función f(x): ")
f_expr = sp.sympify(expr_input)

p0 = float(input("Introduce el valor de p0: "))
p1 = float(input("Introduce el valor de p1: "))
n_iterations = int(input("Introduce el número de iteraciones: "))

x = sp.symbols('x')

pn_values = secant_method(f_expr, p0, p1, n_iterations)


for i, pn in enumerate(pn_values):
    print(f"p_{i} = {pn}")
