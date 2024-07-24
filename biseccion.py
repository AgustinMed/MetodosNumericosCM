import sympy as sp

ITERACIONES = 10000
TOLERANCIA = 0.1e-3

def bisection_method(f_expr, a, b):
    # Convertimos f a una función de Python

    i = 0

    fa = round(f_expr.evalf(subs={x: a}), 15)
    
    while i < ITERACIONES:
        # Calculamos el punto medio p_n
        p_n = (a + b) / 2
        fp = round(f_expr.evalf(subs={x: p_n}), 15)
        
        # Si se encontró la raiz (o cercana) devolver p
        if sp.Abs(fp) < TOLERANCIA:
            return p_n
        
        i += 1

        # Seguir buscando por izq o derecha
        if sp.sign(fa) * sp.sign(fp) > 0:
            a = p_n
            fa = fp
        else:
            b = p_n
    
    return None

# Ingreso de datos por terminal
expr_input = input("Introduce la función f(x): ")
f_expr = sp.sympify(expr_input)

a = float(input("Introduce el valor inicial a: "))
b = float(input("Introduce el valor inicial b: "))

# Definimos la variable simbólica
x = sp.symbols('x')

# Ejecutamos el método de la bisección
root = bisection_method(f_expr, a, b)

# Mostramos el resultado de la raíz
print(f"La raíz aproximada es: {root}")