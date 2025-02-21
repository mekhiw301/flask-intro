# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def do_add():
    """Add a and b from URL query parameters and return result."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a, b))

@app.route('/sub')
def do_sub():
    """Subtract b from a and return result."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a, b))

@app.route('/mult')
def do_mult():
    """Multiply a and b and return result."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a, b))

@app.route('/div')
def do_div():
    """Divide a by b and return result."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a, b))

if __name__ == '__main__':
    app.run(debug=True)
