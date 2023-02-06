import requests
import json
api_url = "http://127.0.0.1:5000/insert/find"

def get(filter):
    api_url = "http://127.0.0.1:5000/insert?filter="
    response = requests.get(api_url + filter)
    if response.status_code != 200:
        print("Not Found", response.status_code)
    else:
        print(response.json())
        print(response.status_code)


def post(todo):
    api_url = "http://127.0.0.1:5000/insert"
    f = open(todo, "r")
    data = json.loads(f.read())
    print(data)
    response = requests.post(url=api_url, json = data)
    if response.status_code != 200:
        print("Not Found", response.status_code)
    else:
        print(response)
        print(response.status_code)

def put(filter, todo):
    api_url = "http://127.0.0.1:5000/update?filter="
    f = open(todo, "r")
    data = json.loads(f.read())
    response = requests.put(api_url + filter, json=todo)
    if response.status_code != 200:
        print("Not Found", response.status_code)
    else:
        print(response)
        print(response.status_code)

def delete(filter):
    api_url = "http://127.0.0.1:5000/remove?filter="
    response = requests.delete(api_url + filter)
    if response.status_code != 200:
        print("Not Found", response.status_code)
    else:
        print(response)
        print(response.status_code)

def main():
    choice = 0
    while choice != 5:
        choice = int(input("Enter a choice: "))
        if choice == 1:
            user = input("Enter PlantType: ")
            get(user)
        elif choice == 2:
            todos = input("Enter data file: ")
            post(todos)
        elif choice == 3:
            user = input("Enter PlantType: ")
            todos = input("Enter updated data: ")
            put(user, todos)
        elif choice == 4:
            user = input("Enter PlantType: ")
            delete(user)
        elif choice == 5:
            quit()
        else:
            print("Invalid")

main()