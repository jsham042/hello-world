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


@app.route('/divide', methods=['GET', 'POST'])
def divide():
    if request.method == 'GET':
        return render_template('divide.html')
    
    try:
        a = float(request.form['a'])
        b = float(request.form['b'])
        response = divide_numbers(a, b)
        if response[1] if isinstance(response, tuple) else 200 == 400:
            # Error case
            error_data = response[0].get_json()
            return render_template('divide.html', error=error_data['error'])
        # Success case
        result_data = response.get_json()
        return render_template('divide.html', result=result_data['result'])
    except (ValueError, KeyError):
        return render_template('divide.html', error='Please provide valid numbers')

@app.route('/api/divide/<float:a>/<float:b>')
def divide_numbers(a, b):
    try:
        if b == 0:
            return jsonify({'error': 'Division by zero is not allowed'}), 400
        result = a / b
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid numbers provided'}), 400