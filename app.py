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

@app.route('/subtract/<int:a>/<int:b>')
def subtract_numbers(a, b):
    return str(a - b)

@app.route('/api/subtract')
def api_subtract():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        result = subtract_numbers(a, b)
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid parameters - both a and b must be integers'}), 400
