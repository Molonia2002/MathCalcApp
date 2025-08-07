import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, lambdify, sympify
import uuid
import os

def plot_graph(expr):
    x = Symbol("x")
    try:
        expression = sympify(expr)
        func = lambdify(x, expression, modules=['numpy'])
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)

        filename = f"{uuid.uuid4().hex}.png"
        path = f"static/{filename}"
        plt.figure()
        plt.plot(x_vals, y_vals, label=f"y = {expr}")
        plt.title("Function Plot")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.savefig(path)
        plt.close()
        return path
    except Exception as e:
        return f"Error: {str(e)}"
