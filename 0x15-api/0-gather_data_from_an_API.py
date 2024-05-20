#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)).json()

    done_tasks = [task for task in todos if task.get('completed') is True]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(user.get('name'), len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))