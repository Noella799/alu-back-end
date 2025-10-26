ther data from an API about an employee's TODO list progress
"""

import requests
import sys


def main():
    """Main function to execute the script"""
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    try:
        # Get employee details
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get('name')
        
        # Get employee TODO list
        todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
        todos_response.raise_for_status()
        todos_data = todos_response.json()
        
        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = []
        
        for task in todos_data:
            if task.get('completed'):
                completed_tasks.append(task)
        
        num_completed_tasks = len(completed_tasks)
        
        # Display progress in required format
        print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
        
        # Display completed task titles
        for task in completed_tasks:
            print(f"\t {task.get('title')}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
