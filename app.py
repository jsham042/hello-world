from flask import Flask, render_template, jsonify
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

@app.route('/divide/<float:a>/<float:b>')
def divide_numbers(a, b):
    try:
        result = a / b
        return jsonify({'result': result})
    except ZeroDivisionError:
        return jsonify({'error': 'Division by zero is not allowed'}), 400

@app.route('/divide/<float:a>/<float:b>')
def divide_numbers(a, b):
    try:
        result = a / b
        return jsonify({'result': result})
    except ZeroDivisionError:
        return jsonify({'error': 'Division by zero is not allowed'}), 400

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    try:
        result = divide_numbers(float(a), float(b))
        return str(result.json['result'])
    except ZeroDivisionError:
        return 'Division by zero is not allowed'
