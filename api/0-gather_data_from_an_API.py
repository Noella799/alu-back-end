#!/usr/bin/python3
""" just using some extra modules """
import requests
import sys


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
