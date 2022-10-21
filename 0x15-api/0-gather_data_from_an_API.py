#!/usr/bin/python3
""" Import request module """
import requests
from sys import argv

id = int(argv[1])

reqTodo = requests.get("https://jsonplaceholder.typicode.com/todos/")
jsonTo = reqTodo.json()
filtered = list(filter(lambda x: x.get('userId') == id, jsonTo))
todoComplete = list(filter(lambda x: x.get('completed'), filtered))

reqUser = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(id))
json = reqUser.json()
name = json.get('name')
print('Employee {} is done with tasks({}/{}):'.format(name, len(todoComplete), len(filtered)))
for i in range(len(todoComplete)):
    print('\t{}'.format(todoComplete[i].get('title')))
