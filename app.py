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

@app.route('/api/sum')
def api_sum():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    
    if num1 is None or num2 is None:
        return jsonify({'error': 'Missing or invalid parameters'}), 400
        
    result = sum_two_numbers(num1, num2)
    return jsonify({'result': result})

def sum_two_numbers(num1, num2):
    return num1 + num2