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

@app.route('/api/subtract')
def subtract():
    try:
        a = float(request.args.get('a', type=float))
        b = float(request.args.get('b', type=float))
        result = a - b
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid parameters. Both a and b must be numbers.'}), 400