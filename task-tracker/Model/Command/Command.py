from Model.Command.ICommand import ICommand


class AddCommand(ICommand):
    def __init__(self, receiver, text):
        self.__receiver = receiver
        self.__text = text

    def execute(self):
        self.__receiver.write(self.__text)


class UpdateStatusTaskCommand(ICommand):
    def __init__(self, receiver, text, cmd):
        self.__receiver = receiver
        self.__text = text
        self.__cmd = cmd

    def execute(self):
        self.__receiver.update_status_task(self.__text, self.__cmd)


class DeleteCommand(ICommand):
    def __init__(self, receiver, text):
        self.__receiver = receiver
        self.__text = text

    def execute(self):
        self.__receiver.delete(self.__text)


class UpdateTaskCommand(ICommand):
    def __init__(self, receiver, id_task, description):
        self.__receiver = receiver
        self.__id_task = id_task
        self.__description = description

    def execute(self):
        self.__receiver.update(self.__id_task, self.__description)


class ListTaskCommand(ICommand):
    def __init__(self, receiver, text=None):
        self.__receiver = receiver
        self.__filter = text

    def execute(self):
        return self.__receiver.read(self.__filter)
