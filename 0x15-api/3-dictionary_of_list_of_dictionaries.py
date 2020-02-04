#!/usr/bin/python3
"""return information about all employees TODO list progress
as a dictionary of lists of dictionarires"""
if __name__ == "__main__":

    import json
    import requests
    import sys

    newdict = {}
    user_id = 1
    for user in range(0, 9):
        ul = []
        req = requests.get(
            "{}{}".format(
                'https://jsonplaceholder.typicode.com/users/', user_id))
        reqdata = req.json()
        todo = requests.get('https://jsonplaceholder.typicode.com/todos')
        tododata = todo.json()
        username = reqdata.get('username')

        for task in tododata:
            if task.get('userId') == int(user_id):
                updatedtask = {}
                updatedtask.update({"username": username})
                updatedtask.update({"task": task.get('title')})
                updatedtask.update({"completed": task.get('completed')})
                ul.append(updatedtask)
        mydict = {str(user_id): ul}
        newdict.update(mydict)
        user_id += 1

    with open('todo_all_employees.json', 'w') as fp:
        dump = json.dump(newdict, fp)
