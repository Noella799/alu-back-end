#!/usr/bin/python3
"""
Script that exports employee TODO list data to JSON format.

This module retrieves employee information and their TODO list from the
JSONPlaceholder REST API and exports the data to a JSON file.
"""

import json
import sys
import urllib.request


def export_employee_todos_to_json(employee_id):
    """
    Fetch employee TODO data and export to JSON file.

    Args:
        employee_id (int): The ID of the employee to fetch data for.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_url = "{}/users/{}".format(base_url, employee_id)
    try:
        with urllib.request.urlopen(user_url) as response:
            user_data = json.loads(response.read().decode())
    except Exception:
        print("Error: Unable to fetch user data")
        return

    username = user_data.get("username")

    # Fetch todos for the user
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    try:
        with urllib.request.urlopen(todos_url) as response:
            todos_data = json.loads(response.read().decode())
    except Exception:
        print("Error: Unable to fetch todos data")
        return

    # Build list of dicts
    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    # Wrap tasks in dictionary keyed by user_id
    data = {str(employee_id): tasks_list}

    # Write to JSON file
    filename = "{}.json".format(employee_id)
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

    print("Data exported to {}".format(filename))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_employee_todos_to_json(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
