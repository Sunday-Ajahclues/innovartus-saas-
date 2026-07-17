from flask import Flask, render_template, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', 
                         time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'uptime': '99.9%',
        'version': '1.0.0'
    })

@app.route('/api/status')
def status():
    return jsonify({
        'service': 'Innovartus SaaS',
        'status': 'operational',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat()
    })

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found', 'status': 404}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Server error', 'status': 500}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
