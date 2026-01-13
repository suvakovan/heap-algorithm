from flask import Flask, render_template, request, jsonify
from task_manager import TaskManager

app = Flask(__name__)
manager = TaskManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(manager.get_all_tasks())

@app.route('/add', methods=['POST'])
def add_task():
    data = request.json
    name = data.get('name')
    priority = data.get('priority')
    
    if name and priority:
        try:
            priority = int(priority)
            manager.add_task(name, priority)
            return jsonify({"success": True, "message": "Task added successfully"})
        except ValueError:
            return jsonify({"success": False, "message": "Invalid priority"}), 400
    return jsonify({"success": False, "message": "Missing data"}), 400

@app.route('/execute', methods=['POST'])
def execute_task():
    task = manager.pop_task()
    if task:
        return jsonify({"success": True, "task": task})
    return jsonify({"success": False, "message": "No tasks to execute"}), 200

@app.route('/get/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    task = manager.get_task(task_id)
    if task:
        return jsonify({"success": True, "task": task})
    return jsonify({"success": False, "message": "Task not found"}), 404

@app.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task_by_id(task_id):
    if manager.delete_task(task_id):
        return jsonify({"success": True, "message": "Task deleted successfully"})
    return jsonify({"success": False, "message": "Task not found"}), 404

@app.route('/update/<int:task_id>', methods=['PUT'])
def update_task_by_id(task_id):
    data = request.json
    new_priority = data.get('priority')
    new_name = data.get('name')
    
    if new_priority is not None:
        try:
            new_priority = int(new_priority)
        except ValueError:
             return jsonify({"success": False, "message": "Invalid priority"}), 400

    if manager.update_task(task_id, new_priority, new_name):
        return jsonify({"success": True, "message": "Task updated successfully"})
    return jsonify({"success": False, "message": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
