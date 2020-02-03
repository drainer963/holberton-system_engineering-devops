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
name = sys.argv[1]

req = requests.get(
    "{}{}".format('https://jsonplaceholder.typicode.com/users/', name))
reqdata = req.json()
username = reqdata['name']
todo = requests.get('https://jsonplaceholder.typicode.com/todos')
tododata = todo.json()

for task in tododata:
    if task['userId'] == int(name):
        count += 1
        ul.append(task)

with open('USER_ID.csv', 'w') as data_file:
    csv_writer = csv.writer(data_file, quoting=csv.QUOTE_ALL)

    for tasks in ul:
        csv_writer.writerow(
            [tasks['userId'], username, tasks['completed'], tasks['title']])
