#!/usr/bin/python3
"""given an employee ID, return information about his/her TODO list progress"""
import json
import requests
import sys

ul = []
user_id = sys.argv[1]

req = requests.get(
    "{}{}".format('https://jsonplaceholder.typicode.com/users/', user_id))
reqdata = req.json()
todo = requests.get('https://jsonplaceholder.typicode.com/todos')
tododata = todo.json()
username = reqdata.get('name')

for task in tododata:
    if task.get('userId') == int(user_id):
        keys_to_exclude = set(('userId', 'id'))
        task = {k: v for k, v in task.items() if k not in keys_to_exclude}
        task.update({"username": username})
        ul.append(task)

mydict = {name: ul}

with open('USER_ID.json', 'w') as fp:
    dump = json.dump(mydict, fp)
