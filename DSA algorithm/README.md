# 🎯 Priority Task Manager

A smart, efficient task scheduling system built with **Python (Flask)** and **Data Structures & Algorithms (Min-Heap)**. This application demonstrates the power of Priority Queues in real-world scenarios, ensuring that critical tasks are always handled first.

---

## 🚀 Overview

The **Priority Task Manager** is a web-based application that allows users to manage their tasks based on urgency. Unlike a standard To-Do list, this system uses a **Min-Heap algorithm** to automatically sort tasks. The task with the highest priority (lowest number, e.g., 1) is always at the top, ready to be executed.

## ✨ Key Features

- **Heap-Based Scheduling:** Automatically sorts tasks by priority using a Min-Heap data structure.
- **Add Tasks:** Create tasks with a name and a priority level (1 = Urgent).
- **Execute Top Task:** "Pop" the highest priority task from the queue with a single click.
- **Dynamic Updates:** Real-time list updates without page reloads.
- **Task Management:** comprehensive CRUD operations (Create, Read, Update, Delete).
- **Responsive UI:** Modern, clean interface with glassmorphism effects.

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask
- **Algorithm:** Min-Heap (Priority Queue) via Python's `heapq` module
- **Frontend:** HTML5, CSS3 (Custom Styles), JavaScript (Fetch API)
- **Styling:** CSS Variables, Flexbox/Grid

## 📦 Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/priority-task-manager.git
    cd priority-task-manager
    ```

2.  **Install Dependencies**
    Ensure you have Python installed. Then run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    ```bash
    python app.py
    ```

4.  **Access the App**
    Open your browser and navigate to:
    `http://127.0.0.1:5000`

## 📖 Usage Guide

1.  **Adding a Task:**
    - Enter a **Task Name** (e.g., "Fix critical bug").
    - Enter a **Priority** number (e.g., `1` for high priority, `10` for low).
    - Click **Add Task**. The list will automatically reorder based on priority.

2.  **Executing a Task:**
    - Click the **Execute Top Priority** button.
    - The system will remove the most urgent task from the queue and display it as "Executed".

3.  **Managing Tasks:**
    - Click **Edit** to change a task's name or priority.
    - Click **Delete** to remove a task entirely.

## 🔌 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/tasks` | Retrieve all pending tasks. |
| `POST` | `/add` | Add a new task (`{"name": "...", "priority": 1}`). |
| `POST` | `/execute` | Execute (pop) the highest priority task. |
| `PUT` | `/update/<id>` | Update an existing task. |
| `DELETE` | `/delete/<id>` | Remove a task by ID. |

## 🧠 algorithmic Insight

This project uses a **Min-Heap** data structure for task management.

- **Why Heap?**
    - **Insertion:** O(log n) - Much faster than sorting a list every time (O(n log n)).
    - **Deletion (Pop Min):** O(log n) - Efficiently retrieves the highest priority element.
    - **Peek (View Min):** O(1) - Instantly see the most urgent task.

This ensures the application remains performant even with a large number of pending tasks, making it ideal for scheduling systems.
