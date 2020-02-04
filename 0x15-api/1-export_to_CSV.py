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
    USER_ID = reqdata.get('id')
    USERNAME = reqdata.get('name')
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    tododata = todo.json()

    for task in tododata:
        if task.get('userId') == int(user_id):
            ul.append(task)

    with open(str(USER_ID) + '.csv', 'w') as data_file:
        csv_writer = csv.writer(data_file, quoting=csv.QUOTE_ALL)

        for tasks in ul:
            TASK_TITLE = tasks.get('title')
            TASK_COMPLETED_STATUS = tasks.get('completed',  False)
            csv_writer.writerow(
                [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])
