# Task Tracker CLI

A beginner-friendly command line app to efficiently manage your to-do list and track tasks.  
Stores all tasks in a simple local JSON file. No third-party dependencies—just Python!

---

## Features

- **Add tasks:** Quickly create new tasks with descriptions.
- **Update tasks:** Edit a task's description by ID.
- **Delete tasks:** Remove a task by its ID.
- **Mark status:** Set tasks as `todo`, `in-progress`, or `done`.
- **List tasks:** Display all tasks, or filter by status (`todo`, `in-progress`, `done`).
- **Persists data:** Tasks are saved in `task.json` in your project directory.
- **Robust:** Prevents errors for empty or missing JSON file.

---

## Getting Started

1. **Requirements:**  
   - Python 3.x installed
   - Run scripts from your terminal (Command Prompt, PowerShell, or PyCharm terminal)

2. **First Run:**  
   The app automatically creates `task.json` as an empty list (`[]`) if it does not exist or is empty.

---

## Usage

Add a new task:

List all tasks:

List only done tasks:

List only todo tasks:

Update a task's description:

Delete a task:

Mark a task in progress:

Mark a task as done:

---

## Project Structure

- `task_tracker.py` : Main CLI application
- `task.json` : JSON file where all tasks are stored
- `README.md` : Project info and instructions

---

## How Tasks Are Stored

Each task is saved as a JSON object with:
- `id` (unique integer)
- `description` (text)
- `status` (`todo`, `in-progress`, `done`)
- `createdAt` (ISO timestamp)
- `updatedAt` (ISO timestamp)

---

## Troubleshooting

- **File not found errors:** The app creates `task.json` automatically.
- **Invalid ID:** Check you’re entering a valid, existing task number (integer).
- **Corrupt JSON:** Open and fix `task.json` manually—ensure it contains valid JSON (at minimum: `[]`).

---

## Author

StrawThePie
