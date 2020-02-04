#!/usr/bin/python3
"""given an employee ID, return information about his/her TODO list progress"""
if __name__ == "__main__":

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
            updatedtask = {}
            updatedtask.update({"task": task.get('title')})
            updatedtask.update({"completed": task.get('completed')})
            updatedtask.update({"username": username})
            ul.append(updatedtask)

    mydict = {user_id: ul}

    with open(str(user_id) + '.json', 'w') as fp:
        dump = json.dump(mydict, fp)
