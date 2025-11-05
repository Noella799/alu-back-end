#!/usr/bin/env python3
"""
Exports an employee's TODO list data to JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    # Fetch user info
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(user_url)
    user = user_response.json()
    username = user.get("username")

    # Fetch todos for the user
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Build JSON data
    user_tasks = []
    for task in todos:
        user_tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {str(user_id): user_tasks}

    # Save to JSON file
    filename = "{}.json".format(user_id)
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

    print("Data exported to {}".format(filename))

