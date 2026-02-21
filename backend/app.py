from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Store submissions in memory (for demo purposes)
submissions = []

@app.route('/api/submit', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('name') or not data.get('email') or not data.get('message'):
            return jsonify({'success': False, 'error': 'All fields are required'}), 400
        
        # Create submission record
        submission = {
            'id': len(submissions) + 1,
            'name': data.get('name'),
            'email': data.get('email'),
            'message': data.get('message'),
            'timestamp': datetime.now().isoformat()
        }
        
        submissions.append(submission)
        
        return jsonify({
            'success': True,
            'message': 'Form submitted successfully',
            'data': submission
        }), 201
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/submissions', methods=['GET'])
def get_submissions():
    try:
        return jsonify({
            'success': True,
            'data': submissions,
            'count': len(submissions)
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'Backend is running'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
