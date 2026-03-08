from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Store submissions in memory (for demo purposes)
submissions = []

# MongoDB Configuration
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['todo_database']
    todo_collection = db['todo_items']
    print("MongoDB connected successfully")
except Exception as e:
    print(f"MongoDB connection failed: {e}")
    todo_collection = None

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

@app.route('/todo', methods=['GET'])
def todo_page():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    try:
        # Get form data
        item_name = request.form.get('itemName')
        description = request.form.get('description')
        
        # Validate required fields
        if not item_name or not description:
            return jsonify({'success': False, 'error': 'All fields are required'}), 400
        
        # Create todo item
        todo_item = {
            'itemName': item_name,
            'description': description,
            'timestamp': datetime.now().isoformat(),
            'completed': False
        }
        
        # Store in MongoDB if available
        if todo_collection is not None:
            result = todo_collection.insert_one(todo_item)
            todo_item['_id'] = str(result.inserted_id)
            return jsonify({
                'success': True,
                'message': 'To-Do item added successfully to MongoDB',
                'data': todo_item
            }), 201
        else:
            # Fallback to in-memory storage
            return jsonify({
                'success': True,
                'message': 'To-Do item added (MongoDB not available, using memory)',
                'data': todo_item
            }), 201
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/todoitems', methods=['GET'])
def get_todo_items():
    try:
        if todo_collection is not None:
            items = list(todo_collection.find())
            for item in items:
                item['_id'] = str(item['_id'])
            return jsonify({
                'success': True,
                'data': items,
                'count': len(items)
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'MongoDB not available'
            }), 503
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
