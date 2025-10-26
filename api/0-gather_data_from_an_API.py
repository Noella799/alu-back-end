#!/usr/bin/python3
<<<<<<< HEAD
"""
using a REST API, and a given emp_ID, return info about their TODO list.
"""
=======
""" just using some extra modules """
>>>>>>> d4948aad6b46cb3aab0a950d21497d0c255858e3
import requests
import sys


<<<<<<< HEAD
if __name__ == "__main__":
    """ main section """
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee = requests.get(
        BASE_URL + f'/users/{sys.argv[1]}/').json()
    EMPLOYEE_NAME = employee.get("name")
    employee_todos = requests.get(
        BASE_URL + f'/users/{sys.argv[1]}/todos').json()
    serialized_todos = {}

    for todo in employee_todos:
        serialized_todos.update({todo.get("title"): todo.get("completed")})

    COMPLETED_LEN = len([k for k, v in serialized_todos.items() if v is True])
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, COMPLETED_LEN, len(serialized_todos)))
    for key, val in serialized_todos.items():
        if val is True:
            print("\t {}".format(key))
=======
def getName():
    """ getting user name """
    payload = {'id': sys.argv[1]}
    dataTwo = requests.get('https://jsonplaceholder.typicode.com/users',
                           params=payload)
    JDataTwo = dataTwo.json()
    # print(JDataTwo[0]['name']
    return JDataTwo[0]['name']


def getTask():
    """ get task numbers and todos done  """
    data = requests.get('https://jsonplaceholder.typicode.com/todos')
    ToDoList = []
    taskToDo = 0
    taskDone = 0
    JData = data.json()
    DataLength = len(JData)
    for i in range(0, DataLength):
        com = int(sys.argv[1])
        if JData[i]['userId'] == com:
            taskToDo += 1
            if JData[i]['completed'] is True:
                ToDoList.append(JData[i]['title'])
                taskDone += 1
    # print(taskToDo)
    # print(taskDone)
    # print(ToDoList)
    print("Employee {} is done with tasks({}/{}):"
          .format(getName(), taskDone, taskToDo))
    Lvalue = len(ToDoList)
    for j in range(0, Lvalue):
        print("\t {}".format(ToDoList[j]))

""" addding docs everywhre """

if __name__ == "__main__":
    """ calling """
    getTask()
>>>>>>> d4948aad6b46cb3aab0a950d21497d0c255858e3
