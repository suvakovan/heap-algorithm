import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_add_task():
    print("Testing Add Task...")
    url = f"{BASE_URL}/add"
    data = {"name": "Test Task", "priority": 1}
    response = requests.post(url, json=data)
    print(response.json())
    return response.status_code == 200

def test_get_tasks():
    print("\nTesting Get All Tasks...")
    url = f"{BASE_URL}/tasks"
    response = requests.get(url)
    tasks = response.json()
    print(f"Tasks: {tasks}")
    return tasks

def test_get_task_by_id(task_id):
    print(f"\nTesting Get Task {task_id}...")
    url = f"{BASE_URL}/get/{task_id}"
    response = requests.get(url)
    print(response.json())
    return response.status_code == 200

def test_update_task(task_id):
    print(f"\nTesting Update Task {task_id}...")
    url = f"{BASE_URL}/update/{task_id}"
    data = {"name": "Updated Task Name", "priority": 5}
    response = requests.put(url, json=data)
    print(response.json())
    return response.status_code == 200

def test_delete_task(task_id):
    print(f"\nTesting Delete Task {task_id}...")
    url = f"{BASE_URL}/delete/{task_id}"
    response = requests.delete(url)
    print(response.json())
    return response.status_code == 200

if __name__ == "__main__":
    try:
        # 1. Add a task
        if test_add_task():
            # 2. Get all to find the ID
            tasks = test_get_tasks()
            if tasks:
                # Assuming the last added task is the one we want to test with
                # The mocked/simple implementation has an incrementing ID starting at 0, 
                # but let's just grab the ID of the last task in the list.
                # Since get_all_tasks returns sorted by priority, we need to find our task.
                # But for simplicity, let's just use the ID from the last element if list not empty.
                target_task = tasks[-1] 
                target_id = target_task['id']
                
                # 3. Inspect
                test_get_task_by_id(target_id)
                
                # 4. Update
                test_update_task(target_id)
                
                # 5. Verify Update
                test_get_task_by_id(target_id)
                
                # 6. Delete
                test_delete_task(target_id)
                
                # 7. Verify Delete
                test_get_task_by_id(target_id) # Should fail
            else:
                print("No tasks found to test.")
    except Exception as e:
        print(f"Test failed: {e}")
