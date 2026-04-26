# Import necessary libraries
import argparse
import json

class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print(f"Task deleted at index {task_index}")
        else:
            print("Invalid task index")

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")

def main():
    parser = argparse.ArgumentParser(description="CLI todo list with persistence")
    parser.add_argument("-a", "--add", help="Add a new task")
    parser.add_argument("-d", "--delete", type=int, help="Delete a task by index")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("--json", action="store_true", help="Output tasks in JSON format")
    parser.add_argument("--output", type=str, help="Write tasks to file")

    args = parser.parse_args()

    todo_manager = TodoManager()

    if args.add:
        todo_manager.add_task(args.add)

    if args.delete:
        todo_manager.delete_task(args.delete - 1)  # Adjust index for list index

    if args.list:
        if args.json:
            print(json.dumps(todo_manager.tasks))
        else:
            todo_manager.list_tasks()

    if args.output:
        with open(args.output, 'w') as file:
            json.dump(todo_manager.tasks, file)

if __name__ == "__main__":
    main()