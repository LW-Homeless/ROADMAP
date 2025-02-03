import argparse
from datetime import datetime

from Model.FileManager import FileManager
from Model.Command import CommandInvoker
from Model.Command.Command import AddCommand, UpdateTaskCommand, DeleteCommand, UpdateStatusTaskCommand, ListTaskCommand
from Model.Task.Task import Task


class Main:

    @staticmethod
    def main():
        filename = "tasktraker.json"
        file_manager = FileManager.FileManager(filename)
        invoke = CommandInvoker.CommandInvoker()

        parser = argparse.ArgumentParser(description="Task Tracker v1.0")
        parser.add_argument("cmd", type=str, choices=['add', 'delete', 'update', 'list',
                                                      'mark-in-progress', 'done'],
                            help="Command for add, delete, update and  list tasks.\nAlso,"
                                 "the command mark-in-progress and done command."
                                 "It allow mark a task like 'in-progress' or 'done'.")
        parser.add_argument("--task", type=str, default="", help="Task id number")
        parser.add_argument("--description", type=str, help="A short description of the task")

        args = parser.parse_args()

        if args.cmd == "add":
            task = Task()
            task.id = task.get_task_id()
            task.description = args.description
            task.status = "TODO"
            task.created_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            task.update_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            text_json = {"id": task.id,
                         "description": task.description,
                         "status": task.status,
                         "createdAt": task.created_at,
                         "updateAt": task.update_at
                         }

            invoke.execute_command(AddCommand(file_manager, text_json))
        elif args.cmd == "update":
            invoke.execute_command(UpdateTaskCommand(file_manager, args.task, args.description))
        elif args.cmd == "delete":
            invoke.execute_command(DeleteCommand(file_manager, args.task))
        elif args.cmd == "mark-in-progress":
            invoke.execute_command(UpdateStatusTaskCommand(file_manager, args.cmd, args.task))
        elif args.cmd == "done":
            invoke.execute_command(UpdateStatusTaskCommand(file_manager, args.cmd, args.task))
        elif args.cmd == "list":
            invoke.execute_command(ListTaskCommand(file_manager, args.task))


if __name__ == '__main__':
    Main.main()
