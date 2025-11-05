#!/usr/bin/python3
"""
Script that exports all employees' TODO list data to JSON format.
"""
import json
import urllib.request


def fetch_json(url):
    """Fetch JSON data from a given URL."""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())


def export_all_todos_to_json():
    """Fetch all users' todos and export to JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"
    all_users = fetch_json(f"{base_url}/users")
    all_todos = {}

    for user in all_users:
        user_id = str(user.get("id"))
        username = user.get("username")
        todos = fetch_json(f"{base_url}/todos?userId={user_id}")

        all_todos[user_id] = []
        for t in todos:
            task_dict = {
                "username": username,
                "task": t.get("title"),
                "completed": t.get("completed")
            }
            all_todos[user_id].append(task_dict)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_todos, json_file)


if __name__ == "__main__":
    export_all_todos_to_json()
