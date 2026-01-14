from flask import Flask, render_template, request, jsonify, Response
from task_manager import TaskManager
from typing import Tuple, Union

app = Flask(__name__)
manager = TaskManager()

@app.route('/')
def index() -> str:
    """Render the main index page."""
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks() -> Response:
    """
    Get all tasks from the manager.
    
    Returns:
        Response: JSON list of tasks.
    """
    return jsonify(manager.get_all_tasks())

@app.route('/add', methods=['POST'])
def add_task() -> Tuple[Response, int]:
    """
    Add a new task via JSON payload.
    
    Expected JSON:
        {
            "name": str,
            "priority": int
        }
        
    Returns:
        Response: Success or error message.
    """
    data = request.json
    name = data.get('name')
    priority = data.get('priority')
    
    if name and isinstance(name, str) and name.strip() and priority:
        try:
            priority = int(priority)
            manager.add_task(name, priority)
            return jsonify({"success": True, "message": "Task added successfully"}), 200
        except ValueError:
            return jsonify({"success": False, "message": "Invalid priority"}), 400
    return jsonify({"success": False, "message": "Missing description or priority"}), 400

@app.route('/execute', methods=['POST'])
def execute_task() -> Response:
    """
    Execute (pop) the highest priority task.
    
    Returns:
        Response: The executed task or a message if queue is empty.
    """
    task = manager.pop_task()
    if task:
        return jsonify({"success": True, "task": task})
    return jsonify({"success": False, "message": "No tasks to execute"}), 200

@app.route('/get/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id: int) -> Tuple[Response, int]:
    """
    Get a specific task by ID.
    
    Returns:
        Response: Task details or not found error.
    """
    task = manager.get_task(task_id)
    if task:
        return jsonify({"success": True, "task": task}), 200
    return jsonify({"success": False, "message": "Task not found"}), 404

@app.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task_by_id(task_id: int) -> Tuple[Response, int]:
    """
    Delete a specific task by ID.
    
    Returns:
        Response: Success message or not found error.
    """
    if manager.delete_task(task_id):
        return jsonify({"success": True, "message": "Task deleted successfully"}), 200
    return jsonify({"success": False, "message": "Task not found"}), 404

@app.route('/update/<int:task_id>', methods=['PUT'])
def update_task_by_id(task_id: int) -> Tuple[Response, int]:
    """
    Update a specific task's details.
    
    Returns:
        Response: Success message or error.
    """
    data = request.json
    new_priority = data.get('priority')
    new_name = data.get('name')
    
    if new_priority is not None:
        try:
            new_priority = int(new_priority)
        except ValueError:
             return jsonify({"success": False, "message": "Invalid priority"}), 400

    if manager.update_task(task_id, new_priority, new_name):
        return jsonify({"success": True, "message": "Task updated successfully"}), 200
    return jsonify({"success": False, "message": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
