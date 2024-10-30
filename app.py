from flask import Flask, jsonify
import psutil
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ping')
def health_check():
    status = 'healthy'
    
    # Check CPU usage
    if psutil.cpu_percent(interval=1) > 90:
        status = 'unhealthy'
    
    # Check memory usage
    if psutil.virtual_memory().percent > 90:
        status = 'unhealthy'
    
    # Check disk usage
    if psutil.disk_usage('/').percent > 90:
        status = 'unhealthy'
    
    # Check external dependency (example: database)
    try:
        # Replace this with your actual database connection check
        requests.get('http://database-url', timeout=5)
    except requests.RequestException:
        status = 'unhealthy'
    
    return jsonify({'status': status})

if __name__ == '__main__':
    app.run(debug=True)