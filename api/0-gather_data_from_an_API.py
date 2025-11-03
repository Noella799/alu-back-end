#!/usr/bin/python3
"""
Using a REST API, and a given emp_ID, return info about their TODO list.
"""
import requests
import sys


if __name__ == "__main__":
    """Main section"""
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    
    # Get employee information
    employee = requests.get(
        BASE_URL + '/users/{}'.format(sys.argv[1])).json()
    EMPLOYEE_NAME = employee.get("name")
    
    # Get employee todos
    employee_todos = requests.get(
        BASE_URL + '/users/{}/todos'.format(sys.argv[1])).json()
    
    # Count completed tasks
    completed_tasks = [todo for todo in employee_todos if todo.get("completed")]
    
    # Print first line
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, len(completed_tasks), len(employee_todos)))
    
    # Print completed task titles with proper formatting (tab + space)
    for todo in completed_tasks:
        print("\t {}".format(todo.get("title")))
