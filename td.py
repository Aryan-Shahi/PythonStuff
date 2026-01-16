
import json

file_name = "todo.json"
# {"tasks": [
#     {"task": "task is this", "complete": True}
    
# ]
# }

def load_tasks():
    try:
        with open(file_name,"r") as file:
            return json.load(file)
    except:
        return {"tasks": []} #empty list

def save_tasks(tasks):
    try:
        with open(file_name,"w") as file: #rewrite or overwrite delete and recreaste  
            json.dump(tasks, file) #takes python dictionary and puts it into file
            
    except:
        return print("failed to save task")


def view_tasks(tasks):
    print()
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display")
    else:
        print("Your tod do list")
        for idx, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx+1}. {task['description']} | {status}")
            print()

def create_task(tasks):
    description = input("Enter the task description: ").strip() #delete leading or trailing white spaces
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("task added")
    else:
        print("Description cannot be empty")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks):
            tasks["tasks"][task_number - 1]["complete'"]= True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")

def main():
    tasks = load_tasks()
    
    
    while True:
        print("To do list manager")
        print("1. View tasks")
        print("2. Add tasks")
        print("3. COmplete  tasks")
        print("4. Exit tasks")
    
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
            
main()