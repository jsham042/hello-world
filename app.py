from flask import Flask, render_template, jsonify, request
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

def subtract_numbers(a, b):
    return a - b

def subtract_numbers(a, b):
    return a - b

@app.route('/subtract')
def subtract():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = subtract_numbers(a, b)
        return str(result)
    except ValueError:
        return "Error: Invalid input - please provide numeric values", 400
