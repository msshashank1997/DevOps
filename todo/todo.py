from flask import Flask, request, jsonify
from typing import List, Dict
import uuid

app = Flask(__name__)

# In-memory storage for to-do items
todos: List[Dict] = []

@app.route('/todos', methods=['POST'])
def create_todo():
    """
    Create a new to-do item
    """
    # Get the request data
    todo_data = request.json
    
    # Validate input
    if not todo_data or 'title' not in todo_data:
        return jsonify({"error": "Title is required"}), 400
    
    # Create a new to-do item with a unique ID
    new_todo = {
        "id": str(uuid.uuid4()),
        "title": todo_data['title'],
        "description": todo_data.get('description', ''),
        "completed": todo_data.get('completed', False)
    }
    
    # Add to the list of todos
    todos.append(new_todo)
    
    return jsonify(new_todo), 201

@app.route('/todos', methods=['GET'])
def get_todos():
    """
    Retrieve all to-do items
    """
    return jsonify(todos)

@app.route('/todos/<string:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """
    Retrieve a specific to-do item by ID
    """
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    
    if todo is None:
        return jsonify({"error": "To-do item not found"}), 404
    
    return jsonify(todo)

@app.route('/todos/<string:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """
    Update a specific to-do item
    """
    # Find the todo item
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    
    if todo is None:
        return jsonify({"error": "To-do item not found"}), 404
    
    # Get update data
    update_data = request.json
    
    # Update the todo item
    todo['title'] = update_data.get('title', todo['title'])
    todo['description'] = update_data.get('description', todo['description'])
    todo['completed'] = update_data.get('completed', todo['completed'])
    
    return jsonify(todo)

@app.route('/todos/<string:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """
    Delete a specific to-do item
    """
    global todos
    
    # Find and remove the todo item
    todos = [todo for todo in todos if todo['id'] != todo_id]
    
    return jsonify({"message": "To-do item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)