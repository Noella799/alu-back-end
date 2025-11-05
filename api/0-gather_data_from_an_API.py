#!/usr/bin/python3
"""
Script that fetches and displays employee TODO list progress from an API.

This module retrieves employee information and their TODO list from the
JSONPlaceholder REST API and displays the progress of completed tasks.
"""
import json
import sys
import urllib.request


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee.

    This function makes API calls to retrieve user information and their
    associated TODO list, then displays the completion progress.

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
    except Exception as e:
        print("Error: Unable to fetch user data")
        return
    
    employee_name = user_data.get('name')
    
    # Fetch todos for the user
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    try:
        with urllib.request.urlopen(todos_url) as response:
            todos_data = json.loads(response.read().decode())
    except Exception as e:
        print("Error: Unable to fetch todos data")
        return
    
    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)
    
    # Display results
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))
    
    # Display completed task titles
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
