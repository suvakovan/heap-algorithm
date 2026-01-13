import heapq

class TaskManager:
    def __init__(self):
        self.task_heap = []
        self.task_id = 0

    def add_task(self, task_name, priority):
        # Storing as (priority, task_id, task_name)
        # task_id serves as a tie-breaker for tasks with the same priority
        heapq.heappush(self.task_heap, (priority, self.task_id, task_name))
        self.task_id += 1
        print(f"Task Added → {task_name} | Priority: {priority}")

    def execute_task(self):
        result = self.pop_task()
        if result:
            print(f"Executing → {result['name']} | Priority: {result['priority']}")
        else:
            print("No tasks to execute")

    def pop_task(self):
        if self.task_heap:
            priority, task_id, task_name = heapq.heappop(self.task_heap)
            return {'priority': priority, 'id': task_id, 'name': task_name}
        return None

    def view_tasks(self):
        tasks = self.get_all_tasks()
        if not tasks:
            print("No pending tasks")
            return
        print("\nPending Tasks:")
        for task in tasks:
            print(f"Task: {task['name']} | Priority: {task['priority']}")

    def get_all_tasks(self):
        # Return sorted list of tasks (copy) without modifying heap
        return [{'priority': t[0], 'id': t[1], 'name': t[2]} for t in sorted(self.task_heap)]

# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task("Prepare for Exam", 1)
    manager.add_task("Complete Assignment", 2)
    manager.add_task("Watch Tutorial", 4)
    manager.add_task("Pay Fees", 1)

    print("\n--- Executing Tasks ---")
    manager.execute_task()
    manager.execute_task()

    print("\n--- Remaining Tasks ---")
    manager.view_tasks()
