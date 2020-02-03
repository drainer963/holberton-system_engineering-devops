#!/usr/bin/python3
"""return information about all employees TODO list progress
as a dictionary of lists of dictionarires"""
import json
import requests
import sys


newdict = {}
name = 1
for user in range(0, 9):
    ul = []
    req = requests.get(
        "{}{}".format('https://jsonplaceholder.typicode.com/users/', name))
    reqdata = req.json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    tododata = todo.json()
    username = reqdata['name']

    for task in tododata:
        if task['userId'] == int(name):
            updatedtask = {}
            updatedtask.update({"username": username})
            updatedtask.update({"task": task['title']})
            updatedtask.update({"completed": task['completed']})
            ul.append(updatedtask)
    mydict = {str(name): ul}
    newdict.update(mydict)
    name += 1

with open('todo_all_employees.json', 'w') as fp:
    dump = json.dump(newdict, fp)
