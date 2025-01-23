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

@app.route('/api/ping')
def api_ping():
    return jsonify({'message': 'Ping!'})

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1, num2):
    try:
        result = num1 / num2
        return str(result)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero", 400
