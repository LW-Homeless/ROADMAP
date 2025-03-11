import json
from datetime import datetime

from tabulate import tabulate


class FileManager:
    def __init__(self, filename):
        self.__filename = filename
        self.__obj_json = []

    def write(self, text):
        try:
            with open(self.__filename, 'r+', encoding='utf-8') as file:
                try:
                    self.__obj_json = json.load(file)
                    self.__obj_json.append(text)
                    file.seek(0)
                    file.truncate()
                    json.dump(self.__obj_json, file, indent=2)
                    file.flush()
                    file.close()
                except json.JSONDecodeError:
                    self.__obj_json = []
                    self.__obj_json.append(text)
                    file.seek(0)
                    file.truncate()
                    json.dump(self.__obj_json, file, indent=2)
                    file.flush()
                    file.close()
            print("[i] Created task success")
        except FileNotFoundError:
            print("[X] File not found")
        finally:
            file.close()

    def read(self, filter=None):

        task = []

        try:
            with open(self.__filename, 'r', encoding='utf-8') as file:
                self.__obj_json = json.load(file)
                file.close()

                if filter == '':
                    task = [[task["id"], task["description"], task["status"], task["createdAt"], task["updateAt"]]
                            for task in self.__obj_json]
                if filter == "done":
                    task = [[task["id"], task["description"], task["status"], task["createdAt"], task["updateAt"]]
                            for task in self.__obj_json if task["status"] == "DONE"]
                if filter == "todo":
                    task = [[task["id"], task["description"], task["status"], task["createdAt"], task["updateAt"]]
                            for task in self.__obj_json if task["status"] == "TODO"]
                if filter == "in-progress":
                    task = [[task["id"], task["description"], task["status"], task["createdAt"], task["updateAt"]]
                            for task in self.__obj_json if task["status"] == "IN PROGRESS"]

                list_task_table = tabulate(task, headers=['ID Task', 'Description', 'State',
                                                          'Created Date', 'Update Date'],
                                           tablefmt="double_grid", maxcolwidths=[None, 30])
                print(list_task_table)
        except FileNotFoundError:
            print("[X] File no found")
        except json.decoder.JSONDecodeError:
            print("[X] There aren't any tasks to display")
        except IndexError:
            print("[X] There aren't any tasks to display")
        finally:
            file.close()

    def update_status_task(self, command, filter=None):
        try:
            if filter.isalpha():
                raise ValueError(f"[X] The task id must be a numeric value other than 0 (zero):{filter}")
            elif isinstance(int(filter), int) and int(filter) == 0:
                raise ValueError(f"[X]The task id must be other than 0 (cero)")
            else:
                cmd = command
                with open(self.__filename, 'r+', encoding='utf-8') as file:
                    self.__obj_json = json.load(file)
                    update_obj_json = self.__obj_json[int(filter) - 1]
                    self.__obj_json.pop(int(filter) - 1)

                    update_obj_json['status'] = ("IN PROGRESS" if cmd == "mark-in-progress"
                                                 else "DONE" if cmd == "done" else "UNKNOWN")

                    update_obj_json['updateAt'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                    self.__obj_json.insert(int(filter) - 1, update_obj_json)
                    file.seek(0)
                    file.truncate()
                    json.dump(self.__obj_json, file, indent=2)
                    file.flush()
                    file.close()
                    print(f"[i] The task ID:{int(filter)} is Updated successfully")
        except FileNotFoundError:
            print("[X] File not found")
        except ValueError as value:
            print(value)
        except IndexError:
            print(f"[X] The task ID:{int(filter)}, Not found")
        finally:
            file.close()

    def delete(self, id_task):
        try:
            if id_task.isalpha():
                raise ValueError(f"[X] The task id must be a numeric value other than 0 (zero):{id_task}")
            elif isinstance(int(id_task), int) and int(id_task) == 0:
                raise ValueError(f"[X] The task id must be other than 0 (cero)")
            else:
                with open(self.__filename, 'r+', encoding='utf-8') as file:
                    self.__obj_json = json.load(file)
                    data = [obj for obj in self.__obj_json if obj["id"] != int(id_task)]
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=2)
                    file.flush()
                    file.close()
                    print(f"[i] The Task ID:{id_task}, deleted.")
        except FileNotFoundError:
            print("[X] File not found")
        except ValueError:
            print(f"[X] The task ID:{id_task} is not valid.")
        except IndexError:
            print(f"[X] The task ID:{int(id_task)} does not exist.")
        finally:
            file.close()

    def update(self, id_task, text):
        try:
            if id_task.isalpha():
                raise ValueError(f"[X] The task id must be a numeric value other than 0 (zero):{id_task}")
            elif isinstance(int(id_task), int) and int(id_task) == 0:
                raise ValueError(f"[X] The task id must be other than 0 (cero)")
            else:
                with open(self.__filename, 'r+', encoding='utf-8') as file:
                    self.__obj_json = json.load(file)

                    data = [{**obj, "description": text,
                             "updateAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S")} if obj["id"] == int(id_task)
                            else obj for obj in self.__obj_json]

                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=2)
                    file.flush()
                    file.close()
                    print(f"[i] The task ID:{id_task}, were update.")
        except FileNotFoundError:
            print("[X] File not found")
        except ValueError:
            print(f"[X] The task ID:{id_task} is not valid.")
        except IndexError:
            print(f"[X] The task ID:{int(id_task)} does not exist.")
        finally:
            file.close()

    def task_id(self):
        try:
            with open(self.__filename, "r", encoding='utf-8') as file:
                try:
                    self.__obj_json = json.load(file)
                    file.close()
                    id_task = self.__obj_json[-1]
                    return id_task['id'] + 1
                except json.JSONDecodeError:
                    file.close()
                    return 1
        except FileNotFoundError:
            print("[X] File not found")
        finally:
            file.close()
