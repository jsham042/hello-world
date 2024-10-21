from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/health', methods=['GET'])
def health_check():
    health_info = {
        'status': 'healthy',
        'environment': 'production',
        'version': '1.0.0'
    }
    return jsonify(health_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)