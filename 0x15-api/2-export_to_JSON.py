#!/usr/bin/python3
"""given an employee ID, return information about his/her TODO list progress"""
import requests
import sys
import json

ul = []
name = sys.argv[1]

req = requests.get(
    "{}{}".format('https://jsonplaceholder.typicode.com/users/', name))
reqdata = req.json()
todo = requests.get('https://jsonplaceholder.typicode.com/todos')
tododata = todo.json()
username = reqdata['name']

for task in tododata:
    if task['userId'] == int(name):
        keys_to_exclude = set(('userId', 'id', 'updated_at'))
        task = {k: v for k, v in task.items() if k not in keys_to_exclude}
        task.update({"username": username})
        ul.append(task)

mydict = {name: ul}

with open('2.json', 'w') as fp:
    dump = json.dump(mydict, fp)
