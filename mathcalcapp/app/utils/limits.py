from sympy import Symbol, sympify, limit

def solve_limit(expr, point):
    x = Symbol("x")
    try:
        expression = sympify(expr)
        return f"Limit as x→{point} is {limit(expression, x, point)}"
    except Exception as e:
        return f"Error: {str(e)}"
