from flask import Blueprint, render_template, request
from .utils.limits import solve_limit
from .utils.continuity import check_continuity
from .utils.functions import evaluate_function
from .utils.graph import plot_graph

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/solve", methods=["POST"])
def solve():
    action = request.form["action"]
    expression = request.form.get("expression")
    point = request.form.get("point", type=float)

    if action == "limit":
        result = solve_limit(expression, point)
    elif action == "continuity":
        result = check_continuity(expression, point)
    elif action == "function":
        result = evaluate_function(expression, point)
    elif action == "plot":
        img_path = plot_graph(expression)
        return render_template("result.html", plot_url=img_path)

    return render_template("result.html", result=result)
