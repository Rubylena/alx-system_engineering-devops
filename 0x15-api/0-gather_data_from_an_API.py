#!/usr/bin/python3
""" Import request module """
import requests
from sys import argv


def userTodo():
    id = int(argv[1])
    api = "https://jsonplaceholder.typicode.com/"
    if (len(argv) > 1):
        reqTodo = requests.get('{}todos/'.format(api)).json()
        filtered = list(filter(lambda x: x.get('userId') == id, reqTodo))
        todoComplete = list(filter(lambda x: x.get('completed'), filtered))

        reqUser = requests.get('{}users/{}'.format(api, id)).json()
        name = reqUser.get('name')
        print('Employee {} is done with tasks({}/{}):'
              .format(name, len(todoComplete), len(filtered)))
        for i in todoComplete:
            print('\t{}'.format(i.get('title')))


if __name__ == '__main__':
    userTodo()
