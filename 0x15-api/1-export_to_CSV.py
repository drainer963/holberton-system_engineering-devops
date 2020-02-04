#!/usr/bin/python3
"""given an employee ID, create a csv file with all tasks assigned to them"""
if __name__ == "__main__":

    import csv
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

    for task in tododata:
        if task.get('userId') == int(user_id):
            ul.append(task)

    with open(str(user_id) + '.csv', 'w') as data_file:
        csv_writer = csv.writer(data_file, quoting=csv.QUOTE_ALL)

        for task in ul:
            csv_writer.writerow(
                [
                    task.get('userId'),
                    reqdata.get('name'),
                    task.get('completed'),
                    task.get('title')
                ])
