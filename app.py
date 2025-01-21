from flask import Flask, render_template, jsonify
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

@app.route('/ping/<target>')
def ping_target(target):
    try:
        output = subprocess.check_output(['ping', '-c', '1', target], text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error pinging {target}: {str(e)}", 500
