import heapq
from typing import List, Dict, Optional, Any, Tuple

class TaskManager:
    """
    A class to manage tasks using a priority queue (min-heap).
    Tasks with lower priority numbers are considered higher priority.
    """
    def __init__(self) -> None:
        """Initialize the TaskManager with an empty heap and task ID counter."""
        self.task_heap: List[Tuple[int, int, str]] = []
        self.task_id: int = 0

    def add_task(self, task_name: str, priority: int) -> None:
        """
        Add a new task to the priority queue.
        
        Args:
            task_name (str): The name of the task.
            priority (int): The priority level (lower value = higher priority).
        """
        # Storing as (priority, task_id, task_name)
        # task_id serves as a tie-breaker for tasks with the same priority
        heapq.heappush(self.task_heap, (priority, self.task_id, task_name))
        self.task_id += 1
        print(f"Task Added → {task_name} | Priority: {priority}")

    def execute_task(self) -> None:
        """Execute (remove and print) the highest priority task."""
        result = self.pop_task()
        if result:
            print(f"Executing → {result['name']} | Priority: {result['priority']}")
        else:
            print("No tasks to execute")

    def pop_task(self) -> Optional[Dict[str, Any]]:
        """
        Remove and return the highest priority task.
        
        Returns:
            Optional[Dict[str, Any]]: A dictionary containing task details, or None if empty.
        """
        if self.task_heap:
            priority, task_id, task_name = heapq.heappop(self.task_heap)
            return {'priority': priority, 'id': task_id, 'name': task_name}
        return None

    def view_tasks(self) -> None:
        """Print all pending tasks sorted by priority."""
        tasks = self.get_all_tasks()
        if not tasks:
            print("No pending tasks")
            return
        print("\nPending Tasks:")
        for task in tasks:
            print(f"Task: {task['name']} | Priority: {task['priority']}")

    def get_all_tasks(self) -> List[Dict[str, Any]]:
        """
        Get all tasks sorted by priority without removing them.
        
        Returns:
            List[Dict[str, Any]]: A list of task dictionaries.
        """
        # Return sorted list of tasks (copy) without modifying heap
        return [{'priority': t[0], 'id': t[1], 'name': t[2]} for t in sorted(self.task_heap)]

    def get_task(self, task_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific task by its ID.
        
        Args:
            task_id (int): The ID of the task to retrieve.
            
        Returns:
            Optional[Dict[str, Any]]: The task dictionary if found, else None.
        """
        for t in self.task_heap:
            if t[1] == task_id:
                return {'priority': t[0], 'id': t[1], 'name': t[2]}
        return None

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id (int): The ID of the task to delete.
            
        Returns:
            bool: True if deleted successfully, False otherwise.
        """
        # Find index of task
        for i, t in enumerate(self.task_heap):
            if t[1] == task_id:
                # Remove and re-heapify
                self.task_heap.pop(i)
                heapq.heapify(self.task_heap)
                return True
        return False

    def update_task(self, task_id: int, new_priority: Optional[int] = None, new_name: Optional[str] = None) -> bool:
        """
        Update a task's priority or name.
        
        Args:
            task_id (int): The ID of the task to update.
            new_priority (Optional[int]): The new priority value.
            new_name (Optional[str]): The new name for the task.
            
        Returns:
            bool: True if updated successfully, False otherwise.
        """
        for i, t in enumerate(self.task_heap):
            if t[1] == task_id:
                priority, tid, name = t
                if new_priority is not None:
                    priority = new_priority
                if new_name is not None:
                    name = new_name
                
                self.task_heap[i] = (priority, tid, name)
                heapq.heapify(self.task_heap)
                return True
        return False

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
