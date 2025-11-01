#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    """Get employee TODO progress"""
    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    # Get user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')
    
    # Get TODOs data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = sum(1 for task in todos_data if task['completed'])
    
    # Display results
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in todos_data:
        if task['completed']:
            print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_employee_todo_progress(int(sys.argv[1]))
