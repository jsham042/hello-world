from flask import Flask, render_template, jsonify
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

@app.route('/add/<int:a>/<int:b>')
def add_numbers_route(a, b):
    return str(add_numbers(a, b))
