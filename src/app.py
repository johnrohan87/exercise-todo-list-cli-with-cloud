import json, requests
todos = []

def get_todos():
    global todos
    return todos

def add_one_task(title):
    # your code here
    temp = {}
    temp.update({
        "label": title,
        "done": False
    })
    todos.append(temp)
    pass

def print_list():
    # your code here
    print(todos)
    if todos != []:
        print("\nThe items currently in memory")
        count = 1
        for things in todos:
            print("Task -" + str(count) + "-> " + str(things["label"]) + " -completed-> " + str(things["done"]))
            count += 1
        pass
    else:
        print("The current list is empty...")

def delete_task(number_to_delete):
    # your code here
    for things in range(len(todos)):
        if int(number_to_delete) == (int(things)-1):
            #print(things)
            #print(todos[int(number_to_delete)-1])
            del todos[int(number_to_delete)-1]
    pass

def initialize_todos():
    global todos
    r = requests.get('https://assets.breatheco.de/apis/fake/todos/user/johnrohan@mail.com') 
    if(r.status_code == 404):
        print("No previous todos found, starting a new todolist")
        print(r)
        if r.status_code == 200:
            print("Tasks initialized successfully")
        elif r.status_code == 500:
            r = requests.post(url = 'https://assets.breatheco.de/apis/fake/todos/user/johnrohan@mail.com', headers = {"Content-Type":"application/json"}, data = [] )
            print("Server response(500) -> " + str(r))
        elif r.status_code == 404:
            r = requests.post(url = 'https://assets.breatheco.de/apis/fake/todos/user/johnrohan@mail.com', headers = {"Content-Type":"application/json"}, data = [] )
            print("Server response(404) -> " + str(r))
    else:
        print("A todo list was found, loading the todos...")
        todos = r.json()

    
def save_todos():
    # your code here
    print(todos)
    temp = json.dumps(todos)
    #print(temp)
    r = requests.put(url = 'https://assets.breatheco.de/apis/fake/todos/user/johnrohan@mail.com', headers = {"Content-Type":"application/json"}, data = temp)
    print(r.json())
    print(r)
    pass

def load_todos():
    # your code here
    r = requests.get('https://assets.breatheco.de/apis/fake/todos/user/johnrohan@mail.com') 
    todos = r.json()
    print(todos)
    pass
    
# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    stop = False
    print("Initializing todos with previous data or creating a new todo's list...")
    initialize_todos()
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Send/Save todo's to API
        5. Retrieve todo's from API
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print_list()
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")