Sample solution for the [task-tracker](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh)

# Task Tracker

Task tracker is a project used to track and manage your tasks. A simple command line interface will be built to keep track of what needs to be done. What you have done and what you are currently working on. This project will help you practice your programming skills including working with the file system, handling user input, and building a simple CLI application.

# Requirements
The application should run from the command line, accept user input and actions as arguments, and store tasks in a JSON file. The user should be able to:
- Add, update, and delete tasks..
- Mark a task as "in progress" or "done".
- List all tasks done.
- List all the tasks that are not done.
- List all tasks that are in progress.

**Task Properties**
Each task should have the following properties.
- **id:** A unique identifier for the task.
- **description:** A short description of the task.
- **status:** The status of the task (todo, in-progress, done).
- **createdAt:** The date and time when the task was created.
- **updatedAt:** The date and time when the task was last updated.

# Solution
- Programming language: Python 3.11.3.
- Type of programming: object-oriented programming (OOP).
- Design pattern: Behavioral design pattern **Command**.

The **Command** design pattern has the following structure.
![alt text](https://github.com/LW-Homeless/roadmap/blob/main/backend/task-tracker/structure.png)

# How to use
Install tabulate module with the following command: pip install tabulate==0.9.0

- **Add to task :** python task-cli.py add --description "Test"
- **Delete task :** python task-cli.py delete --task 1
- **Update task :** python task-cli.py update --task 1 --description "Test Update"
- **Mark a task as "in progress" :** python task-cli.py mark-in-progress --task 1
- **Mark a task as "done" :** python task-cli.py done --task 1
- **List all tasks :** python task-cli.py list
- **List all tasks that are done :** python task-cli.py list --task "done"
- **List all tasks that are in progress :** python task-cli.py list --task "in-progress"
- **List all task that are todo :** python task-cli.py list --task "todo"

![alt text](https://github.com/LW-Homeless/roadmap/blob/main/backend/task-tracker/video.gif)
