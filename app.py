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
    """Return the difference between two numbers."""
    return a - b

@app.route('/subtract')
def subtract():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        return str(subtract_numbers(a, b))
    except ValueError:
        return "Error: Parameters must be integers"