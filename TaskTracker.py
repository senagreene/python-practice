
import json
import datetime
import os


class Task:

    def __init__(self, desc, name, status, id):
        self.name = name
        self.status = status
        self.desc = desc
        self.id = id
        self.createdAt = datetime.datetime.now()

    def __str__(self):
        return f"Task(id={self.id},name ={self.name},status={self.status},description= {self.desc},createdAt= {self.createdAt})"


tasks = []
file_path = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file if it exists."""
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
            for task_data in data:
                task = Task(task_data['desc'], task_data['name'],
                            task_data['status'], task_data['id'])
                task.createdAt = datetime.datetime.strptime(
                    task_data['createdAt'], "%Y-%m-%d %H:%M:%S.%f")
                tasks.append(task)


def save_tasks():
    """Save tasks to the JSON file."""
    with open(file_path, "w") as f:
        data = [{
            'desc': task.desc,
            'name': task.name,
            'status': task.status,
            'id': task.id,
            'createdAt': task.createdAt.strftime("%Y-%m-%d %H:%M:%S.%f")
        } for task in tasks]
        json.dump(data, f, indent=4)


def addTask():

    name = input("enter task: ")
    desc = input("enter task description: ")
    status = "todo"
    task = Task(name=name, desc=desc, id=len(tasks), status=status)
    tasks.append(task)
    save_tasks()
    print(f"Task'{task}' has been added.The task id is {task.id} ")


def listTask():
    if tasks:
        for task in tasks:
            print(task)


def deleteTask():
    deleteTask = input("Please enter the task or its ID to delete: ")
    # if the input is task id
    if deleteTask.isdigit():
        index = int(deleteTask)
        if 0 <= index < len(tasks):
            deleteTask = tasks.pop(index)
            save_tasks()
            print(f"the task {deleteTask} has been deleted")
        else:
            print("Invalid task ID.Please try again")

    # If the input is task's name
    else:

        dtask = next(
            (task for task in tasks if task.name == deleteTask), None)
        if dtask:
            tasks.remove(dtask)
            save_tasks()
            print(f"the task {dtask} has been deleted")
        else:
            print("Invalid input.Please try again")


def updateTask():
    updatedAt = datetime.datetime.now()
    user_input = input("Please enter the task or its ID to update:")

    # if the input is task id
    if user_input.isdigit():
        index = int(user_input)
        if 0 <= index < len(tasks):
            task = tasks[index]
            updatedName = input("Enter a new task name: ")
            updatedDesc = input("Enter a new task description: ")
            task.name = updatedName
            task.desc = updatedDesc
            save_tasks()
            print(f"the task updated to:{task}")
        else:
            print("Invalid task ID.Please try again")
     # If the input is task's name
    else:
        utask = next(
            (task for task in tasks if task.name == user_input), None)
        if utask:
            updatedName = input("Enter a new task name: ")
            updatedDesc = input("Enter a new task description: ")
            utask.name = updatedName
            utask.desc = updatedDesc
            save_tasks()
            print(f"the task updated to:{utask}")
        else:
            print("Invalid task ID.Please try again")


def markTask():
    user_input = input("Please enter the task or its ID: ")

    # if the input is task id
    if user_input.isdigit():
        index = int(user_input)
        if 0 <= index < len(tasks):
            task = tasks[index]
            newStatus = input("Enter new task status(todo/in progress/done): ")
            task.status = newStatus
            save_tasks()
            print(f"task status updated:{task}")
        else:
            print("Invalid task ID.Please try again")
     # if the input is task's name
    else:
        taskUpdate = next(
            (task for task in tasks if task.name == user_input), None)
        if taskUpdate:
            newStatus = input("Enter new task status(todo/in progress/done): ")
            taskUpdate.status = newStatus
            save_tasks()
            print(f"the task status updated to:{taskUpdate}")
        else:
            print("Invalid task ID.Please try again")


def main():
    while True:
        print("\n Task Manager")
        print("Add Task 1")
        print("List Tasks 2")
        print("Delete Task 3")
        print("Mark Task Status 4")
        print("Update Task 5")
        print("Exit 6")

        choice = input("enter your choice(1-6)")

        if choice == '1':
            addTask()
        elif choice == '2':
            listTask()
        elif choice == '3':
            deleteTask()
        elif choice == '4':
            markTask()
        elif choice == '5':
            updateTask()
        elif choice == '6':
            print("exiting task manager")
            break
        else:
            print("Invalid choice.Enter a number between 1 and 6")


if __name__ == "__main__":
    main()
