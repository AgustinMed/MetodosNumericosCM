import sympy as sp

def newton_raphson_sympy(expr_str, x0, tol=1e-7, max_iter=100):
    """
    Implementa el método de Newton-Raphson usando sympy para encontrar la raíz de una función.

    :param expr_str: La expresión de la función de la cual se busca la raíz en formato string.
    :param x0: La estimación inicial.
    :param tol: La tolerancia para el criterio de convergencia.
    :param max_iter: El número máximo de iteraciones permitidas.
    :return: La raíz estimada.
    """
    # Definir la variable y convertir la expresión a una expresión simbólica
    x = sp.symbols('x')
    expr = sp.sympify(expr_str)
    
    # Derivar la función
    f_prime = sp.diff(expr, x)
    
    # Convertir las expresiones simbólicas a funciones numéricas
    f = sp.lambdify(x, expr, "numpy")
    df = sp.lambdify(x, f_prime, "numpy")
    
    # Estimación inicial
    x_n = x0
    for n in range(max_iter):
        fx_n = f(x_n)
        dfx_n = df(x_n)
        
        if dfx_n == 0:
            raise ValueError("La derivada es cero en x = {}. El método no puede continuar.".format(x_n))
        
        x_n1 = x_n - fx_n / dfx_n
        
        if abs(x_n1 - x_n) < tol:
            return x_n1
        
        x_n = x_n1
    
    raise ValueError("El método de Newton-Raphson no convergió después de {} iteraciones".format(max_iter))

# Ejemplo de uso
if __name__ == "__main__":
    print("Introduce la función f(x): ")
    print("Ejemplos de funciones válidas:")
    print(" - x**2 para x al cuadrado")
    print(" - sqrt(x) o x**0.5 para la raíz cuadrada de x")
    print(" - log(x) para el logaritmo natural de x")
    print(" - sin(x), cos(x), tan(x) para las funciones trigonométricas")
    print(" - exp(x) para la función exponencial")
    
    # Solicitar la expresión de la función al usuario
    expr_str = input("Introduce la expresión de la función: ")
    
    # Solicitar la estimación inicial al usuario
    x0 = float(input("Introduce la estimación inicial: "))
    
    # Encontrar la raíz
    try:
        raiz = newton_raphson_sympy(expr_str, x0)
        print("La raíz estimada es:", raiz)
    except ValueError as e:
        print(e)
