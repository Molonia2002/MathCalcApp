from sympy import Symbol, sympify

def evaluate_function(expr, point):
    x = Symbol("x")
    try:
        expression = sympify(expr)
        result = expression.subs(x, point)
        return f"f({point}) = {result}"
    except Exception as e:
        return f"Error: {str(e)}"
