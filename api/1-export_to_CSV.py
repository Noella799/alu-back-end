#!/usr/bin/python3
"""
Script that exports employee TODO list data to CSV format.

This module retrieves employee information and their TODO list from the
JSONPlaceholder REST API and exports the data to a CSV file.
"""
import csv
import json
import sys
import urllib.request


def export_employee_todos_to_csv(employee_id):
    """
    Fetch employee TODO data and export to CSV file.

    This function makes API calls to retrieve user information and their
    associated TODO list, then exports all tasks to a CSV file named
    after the employee ID.

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

    username = user_data.get('username')

    # Fetch todos for the user
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    try:
        with urllib.request.urlopen(todos_url) as response:
            todos_data = json.loads(response.read().decode())
    except Exception as e:
        print("Error: Unable to fetch todos data")
        return

    # Export to CSV
    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow([
                str(employee_id),
                username,
                str(task.get('completed')),
                task.get('title')
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_employee_todos_to_csv(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
