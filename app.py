from flask import Flask, render_template, jsonify, request
import random
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
    min_val = request.args.get('min', 1, type=int)
    max_val = request.args.get('max', 100, type=int)
    return jsonify({'number': random.randint(min_val, max_val)})
