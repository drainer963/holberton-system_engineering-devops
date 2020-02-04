#!/usr/bin/python3
"""given an employee ID, create a csv file with all tasks assigned to them"""
import csv
import json
import requests
import sys

count = 0
ccount = 0
ul = []
cl = []
user_id = sys.argv[1]

req = requests.get(
    "{}{}".format('https://jsonplaceholder.typicode.com/users/', user_id))
reqdata = req.json()
username = reqdata.get('name')
todo = requests.get('https://jsonplaceholder.typicode.com/todos')
tododata = todo.json()

for task in tododata:
    if task.get('userId') == int(user_id):
        count += 1
        ul.append(task)

with open('USER_ID.csv', 'w') as data_file:
    csv_writer = csv.writer(data_file, quoting=csv.QUOTE_ALL)

    for tasks in ul:
        csv_writer.writerow(
            [tasks.get('userId'), username, tasks.get('completed'),
             tasks.get('title')])
