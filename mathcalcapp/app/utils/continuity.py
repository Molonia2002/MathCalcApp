from sympy import Symbol, sympify, limit

def check_continuity(expr, point):
    x = Symbol("x")
    try:
        expression = sympify(expr)
        left = limit(expression, x, point, dir='-')
        right = limit(expression, x, point, dir='+')
        value = expression.subs(x, point)

        if left == right == value:
            return f"The function is continuous at x = {point}"
        else:
            return f"Discontinuous at x = {point}: Left={left}, Right={right}, Value={value}"
    except Exception as e:
        return f"Error: {str(e)}"
