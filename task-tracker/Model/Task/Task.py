from Model.FileManager.FileManager import FileManager


class Task:
    def __init__(self):
        self.__id = ""
        self.__description = ""
        self.__status = ""
        self.__created_at = ""
        self.__update_at = ""

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, create_at):
        self.__created_at = create_at

    @property
    def update_at(self):
        return self.__update_at

    @update_at.setter
    def update_at(self, update_at):
        self.__update_at = update_at

    def get_task_id(self):
        task_id = FileManager('tasktraker.json')
        return task_id.task_id()

