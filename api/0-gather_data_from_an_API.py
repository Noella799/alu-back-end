#!/usr/bin/python3
"""
Script that uses REST API to return employee TODO list progress.
For a given employee ID, displays completed tasks information.
"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    
    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get("{}/todos".format(base_url),
                         params={"userId": user_id}).json()
    
    completed = [task for task in todos if task.get("completed") is True]
    
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    
    for task in completed:
        print("\t {}".format(task.get("title")))
