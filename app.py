from flask import Flask, render_template, jsonify
from datetime import datetime

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

@app.route('/ping_with_timestamp')
def ping_with_timestamp():
    current_time = datetime.now().isoformat()
    return jsonify({
        'message': 'Ping!',
        'timestamp': current_time
    })