from flask import Flask, render_template, jsonify
import subprocess
from ping3 import ping, PingError
import socket
import re
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
        # Validate input
        if not target or len(target) > 255:  # DNS names can't be longer than 255 characters
            return jsonify({'error': 'Invalid hostname or IP address length'}), 400
            
        # Check if it's an IP address
        try:
            socket.inet_pton(socket.AF_INET, target)  # IPv4
        except socket.error:
            try:
                socket.inet_pton(socket.AF_INET6, target)  # IPv6
            except socket.error:
                # Check if it's a valid hostname
                if not re.match(r'^[a-zA-Z0-9-\.]+$', target):  # Basic hostname chars
                    return jsonify({'error': 'Invalid hostname characters'}), 400
                try:
                    socket.gethostbyname(target)
                except socket.gaierror:
                    return jsonify({'error': 'Unable to resolve hostname'}), 400
        
        response_time = ping(target)
        if response_time is None:
            return jsonify({'error': f'Could not reach host {target}'}), 404
        if response_time is False:
            return jsonify({'error': f'Invalid hostname or IP address: {target}'}), 400
            
        return jsonify({
            'target': target,
            'response_time_ms': round(response_time * 1000, 2)
        })
    except PingError as e:
        return jsonify({'error': f'Ping error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500
