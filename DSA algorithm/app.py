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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
