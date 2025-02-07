from flask import Flask, render_template, jsonify, request

from math_utils import subtract_numbers, add_numbers, multiply_numbers, divide_numbers

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/ping')
def ping():
    return 'Ping!'

@app.route('/pong')
def pong():
    return 'pong'

@app.route('/show_ping')
def show_ping():
    return render_template('ping.html')

@app.route('/api/ping')
def api_ping():
    return jsonify({'message': 'Ping!'})

@app.route('/subtract')
def subtract():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = subtract_numbers(a, b)
        return str(result)
    except ValueError:
        return "Error: Invalid input - please provide numeric values", 400

@app.route('/add')
def add():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = add_numbers(a, b)
        return str(result)
    except ValueError:
        return "Error: Invalid input - please provide numeric values", 400

@app.route('/multiply')
def multiply():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = multiply_numbers(a, b)
        return str(result)
    except ValueError:
        return "Error: Invalid input - please provide numeric values", 400

@app.route('/divide')
def divide():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = divide_numbers(a, b)
        return str(result)
    except ValueError as e:
        if "Cannot divide by zero" in str(e):
            return "Error: Cannot divide by zero", 400
        return "Error: Invalid input - please provide numeric values", 400
