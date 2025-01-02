from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

def add_numbers(a, b):
    return a + b

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

@app.route('/add')
def add():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is None or b is None:
        return jsonify({'error': 'Please provide both "a" and "b" parameters as integers'}), 400
    result = add_numbers(a, b)
    return jsonify({'result': result})