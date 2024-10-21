from flask import Flask, jsonify
import time
import psutil

app = Flask(__name__)

# Application start time
start_time = time.time()

# Application version
VERSION = "1.0.0"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/health')
def health_check():
    # Calculate uptime in seconds
    uptime = int(time.time() - start_time)
    
    # Check database connectivity (Placeholder for actual implementation)
    try:
        # Example: Replace with actual database connection check
        db_connected = True  # Assume the database is connected
    except Exception:
        db_connected = False

    # Get memory usage in MB
    process = psutil.Process()
    memory_usage_mb = round(process.memory_info().rss / (1024 * 1024), 2)
    
    health_data = {
        "status": "healthy",
        "uptime_seconds": uptime,
        "application_version": VERSION,
        "database_connectivity": db_connected,
        "memory_usage_mb": memory_usage_mb
    }
    
    return jsonify(health_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)