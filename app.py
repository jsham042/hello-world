from flask import Flask, render_template, jsonify
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


@app.route('/random')
def random_number():
    return str(random.randint(1, 10000))

@app.route('/api/ping')
def api_ping():
    return jsonify({'message': 'Ping!'})