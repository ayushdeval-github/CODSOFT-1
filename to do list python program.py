#to do list python program
import sys
tasks=[]
def desplay_menu():
  print("\nto do list application")
  print("1. add task")
  print("2. view tasks")
  print("3. mark task as complete")
  print("4. delete task")
  print("5. quit")
def add_task():
  task = input("enter task: ")
  tasks.append({"task": task, "completed": False})
  print("task added successfully")
def view_tasks():
  if not tasks:
    print("No tasks in the list.")
  else:
    print("\nTasks:")
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. {task['task']} [{status}]")
def mark_task_complete():
  view_tasks()
  task_number = int(input("Enter the task number to mark as completed: "))
  if 0 < task_number <= len(tasks):
      tasks[task_number - 1]["completed"] = True
      print(f'Task "{tasks[task_number - 1]["task"]}" marked as completed.')
  else:
      print("Invalid task number.")
def delete_task():
  view_tasks()
  task_index = int(input("enter the task number to delete: "))
  if 1 <= task_index <= len(tasks):
    tasks.pop(task_index - 1)
    print("task deleted")
  else:
    print("invalid task number")
def main():
  while True:
    desplay_menu()
    choice = input("enter your choice: ")
    if choice == "1":
      add_task()
    elif choice == "2":
      view_tasks()
    elif choice == "3":
      mark_task_complete()
    elif choice == "4":
      delete_task()
    elif choice == "5":
      print("goodbye")
      sys.exit()
    else:
      print("invalid choice")
if __name__ == "__main__":
  main()
