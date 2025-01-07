import random
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

@app.route('/random')
def random_number():
    min_val = request.args.get('min', default=1, type=int)
    max_val = request.args.get('max', default=1000, type=int)
    number = random.randint(min_val, max_val)
    return jsonify({'number': number})