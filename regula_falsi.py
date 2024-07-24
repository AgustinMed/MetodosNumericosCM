import sympy as sp

def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    x = sp.symbols('x')
    f_expr = sp.sympify(f)
    f_a = f_expr.subs(x, a)
    f_b = f_expr.subs(x, b)
    
    if f_a * f_b >= 0:
        raise ValueError("La función debe tener signos diferentes en los puntos a y b")
    
    for i in range(max_iter):
        p = b - (f_b * (b - a)) / (f_b - f_a)
        f_p = f_expr.subs(x, p)
        
        if abs(f_p) < tol:
            return p.evalf()
        
        if f_a * f_p < 0:
            b, f_b = p, f_p
        else:
            a, f_a = p, f_p
    
    raise ValueError("El método no convergió en el número máximo de iteraciones")

if __name__ == "__main__":
    print("Ejemplos de funciones válidas:")
    print(" - x**2 para x al cuadrado")
    print(" - sqrt(x) o x**0.5 para la raíz cuadrada de x")
    print(" - log(x) para el logaritmo natural de x")
    print(" - sin(x), cos(x), tan(x) para las funciones trigonométricas")
    print(" - exp(x) para la función exponencial")
    funcion = input("Introduce la función en términos de x (por ejemplo, 'x**3 - x - 2'): ")

    a = float(input("Introduce el valor de a: "))
    b = float(input("Introduce el valor de b: "))
    tolerancia = float(input("Introduce la tolerancia (por defecto 1e-6): ") or 1e-6)

    try:
        raiz = regula_falsi(funcion, a, b, tol=tolerancia)
        print(f"La raíz encontrada es: {raiz}")
    except ValueError as e:
        print(e)
