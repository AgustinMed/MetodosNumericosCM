import sympy as sp

def punto_fijo(g, aprox, tol=1e-6, max_iter=100):
    x = sp.symbols('x')
    g_expr = sp.sympify(g)
    
    for i in range(max_iter):
        p = g_expr.subs(x, aprox)
        
        if abs(p - aprox) < tol:
            return p.evalf()
        
        aprox = p
    
    raise ValueError("El método no convergió en el número máximo de iteraciones")

if __name__ == "__main__":
    print("Ejemplos de funciones válidas:")
    print(" - x**2 para x al cuadrado")
    print(" - sqrt(x) o x**0.5 para la raíz cuadrada de x")
    print(" - log(x) para el logaritmo natural de x")
    print(" - sin(x), cos(x), tan(x) para las funciones trigonométricas")
    print(" - exp(x) para la función exponencial")
    funcion_g = input("Introduce la función g(x): ")
    aprox = float(input("Introduce el valor inicial: "))
    tolerancia = float(input("Introduce la tolerancia (por defecto 1e-6): ") or 1e-6)

    try:
        raiz = punto_fijo(funcion_g, aprox, tol=tolerancia)
        print(f"La raíz encontrada es: {raiz}")
    except ValueError as e:
        print(e)
