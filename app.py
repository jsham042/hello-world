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

def add_numbers(a: float, b: float) -> float:
    return a + b

@app.route('/add')
def add():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    result = add_numbers(num1, num2)
    return render_template('add.html', result=result)