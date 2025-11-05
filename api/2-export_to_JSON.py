#!/usr/bin/python3
"""
Module 2-export_to_JSON

Exports all tasks of a given employee ID to a JSON file in the format:

{
    "<USER_ID>": [
        {"task": "TASK_TITLE", "completed": COMPLETED_STATUS,
         "username": "USERNAME"},
        ...
    ]
}

Usage:
    ./2-export_to_JSON.py <employee_id>
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    # Fetch user information
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(user_url)
    user = response.json()
    username = user.get("username")

    # Fetch all tasks for the user
    todos_url = (
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    )
    response = requests.get(todos_url)
    todos = response.json()

    # Build list of dicts
    tasks_list = []
    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks_list.append(task_dict)

    # Wrap in dictionary with user_id as key
    data = {str(user_id): tasks_list}

    # Save to JSON file
    filename = "{}.json".format(user_id)
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

    print("Data exported to {}".format(filename))

