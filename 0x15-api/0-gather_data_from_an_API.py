#!/usr/bin/python3
"""given an employee ID, return information about his/her TODO list progress"""
import json
import requests
import sys

count = 0
ccount = 0
ul = []
cl = []
name = sys.argv[1]

req = requests.get(
    "{}{}".format('https://jsonplaceholder.typicode.com/users/', name))
reqdata = req.json()
todo = requests.get('https://jsonplaceholder.typicode.com/todos')
tododata = todo.json()

for task in tododata:
    if task['userId'] == int(name):
        count += 1
        ul.append(task)

for task in ul:
    if task['completed'] is True:
        ccount += 1
        cl.append(task)

print("{} {} {}({}/{}):".format(
    "Employee", reqdata['name'], "is done with tasks", ccount, count))

for tasks in cl:
    print("{} {}".format('\t', tasks['title']))
