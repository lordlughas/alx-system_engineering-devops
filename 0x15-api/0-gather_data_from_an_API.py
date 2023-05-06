#!/usr/bin/python3
"""script using REST API to reurn information of employee ID"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [td.get("title") for td in todos if td.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
    user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]


