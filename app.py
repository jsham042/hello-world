from flask import Flask, render_template, jsonify, request
import subprocess
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

@app.route('/ping_host')
def ping_host():
    host = request.args.get('host')
    if not host:
        return jsonify({'error': 'Host parameter is required'}), 400
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], text=True)
        return jsonify({'output': output})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': f'Ping failed: {str(e)}'}), 500