import json
import os

TASKS_FILE = "tasks.json"
PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(task_list):
    with open(TASKS_FILE, "w") as file:
        json.dump(task_list, file, indent=2)


def add_task(title, subject, deadline, priority):
    task_list = load_tasks()
    new_id = max([t["id"] for t in task_list], default=0) + 1
    task = {"id": new_id, "title": title, "subject": subject,
            "deadline": str(deadline), "priority": priority, "done": False}
    task_list.append(task)
    save_tasks(task_list)
    return task

def get_sorted_tasks(subject="All"):
    task_list = load_tasks()
    if subject != "All":
        task_list = [t for t in task_list if t["subject"] == subject]
    return sorted(task_list, key=lambda t: (t["done"], PRIORITY_ORDER[t["priority"]], t["deadline"]))