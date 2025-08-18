import os
import json
import sys
from datetime import datetime

FILENAME = "task.json"


# ----------------------
# Utility Functions
# ----------------------

def ensure_json_file():
    """Ensures JSON file exists and contains valid JSON ([])."""
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        with open(FILENAME, "w") as f:
            json.dump([], f)


def load_tasks():
    """Loads tasks from the JSON file. Returns empty list if file is invalid/empty."""
    if os.path.getsize(FILENAME) == 0:
        return []
    with open(FILENAME, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    """Saves tasks to the JSON file with pretty formatting."""
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)


# ----------------------
# Core Task Operations
# ----------------------

def list_tasks(filter_status=None):
    """Prints a table of tasks, optionally filtered by status."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]

    print(f"{'ID':<4} {'Status':<12} {'Description':<40} {'Updated At'}")
    print("-" * 70)
    for task in tasks:
        print(f"{task['id']:<4} {task['status']:<12} {task['description']:<40} {task['updatedAt']}")


def add_task(description):
    """Adds a new task with the given description."""
    tasks = load_tasks()
    new_id = max([task["id"] for task in tasks], default=0) + 1
    now = datetime.now().isoformat(timespec='seconds')
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Added new task #{new_id}: {description}")


def update_task(task_id, new_description):
    """Updates a task's description by its ID."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat(timespec='seconds')
            save_tasks(tasks)
            print(f"Task #{task_id} updated: {new_description}")
            return
    print(f"No task found with ID {task_id}.")


def delete_task(task_id):
    """Deletes a task by its ID."""
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"No task found with ID {task_id}.")
    else:
        save_tasks(new_tasks)
        print(f"Task #{task_id} deleted.")


def mark_task_status(task_id, status):
    """Updates a task's status (todo, in-progress, done) by ID."""
    valid_status = ["todo", "in-progress", "done"]
    if status not in valid_status:
        print(f"Invalid status '{status}'. Choose from {valid_status}.")
        return
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat(timespec='seconds')
            save_tasks(tasks)
            print(f"Task #{task_id} marked as {status}.")
            return
    print(f"No task found with ID {task_id}.")


# ----------------------
# Command Line Interface
# ----------------------

def main():
    ensure_json_file()

    if len(sys.argv) > 1:
        cmd = sys.argv[1]

        if cmd == "add":
            if len(sys.argv) < 3:
                print('Usage: python task_tracker.py add "your task description"')
            else:
                desc = " ".join(sys.argv[2:])
                add_task(desc)

        elif cmd == "update":
            if len(sys.argv) < 4:
                print('Usage: python task_tracker.py update <id> "new description"')
            else:
                try:
                    task_id = int(sys.argv[2])
                    new_desc = " ".join(sys.argv[3:])
                    update_task(task_id, new_desc)
                except ValueError:
                    print("Task ID must be an integer.")

        elif cmd == "delete":
            if len(sys.argv) < 3:
                print('Usage: python task_tracker.py delete <id>')
            else:
                try:
                    task_id = int(sys.argv[2])
                    delete_task(task_id)
                except ValueError:
                    print("Task ID must be an integer.")

        elif cmd == "mark-in-progress":
            if len(sys.argv) < 3:
                print('Usage: python task_tracker.py mark-in-progress <id>')
            else:
                try:
                    task_id = int(sys.argv[2])
                    mark_task_status(task_id, "in-progress")
                except ValueError:
                    print("Task ID must be an integer.")

        elif cmd == "mark-done":
            if len(sys.argv) < 3:
                print('Usage: python task_tracker.py mark-done <id>')
            else:
                try:
                    task_id = int(sys.argv[2])
                    mark_task_status(task_id, "done")
                except ValueError:
                    print("Task ID must be an integer.")

        elif cmd == "list":
            status_filter = sys.argv[2] if len(sys.argv) > 2 else None
            valid_status = ["todo", "in-progress", "done"]
            if status_filter and status_filter not in valid_status:
                print(f"Invalid status filter. Use one of: {valid_status}")
            else:
                list_tasks(status_filter)

        else:
            print("Unknown command.")
    else:
        print('Usage: python task_tracker.py add "your task description"')

if __name__ == "__main__":
    main()
