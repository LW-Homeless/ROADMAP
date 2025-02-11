from .ICommand import ICommand


class GetEventUser(ICommand):
    def __init__(self, receiver, query):
        self.__receiver = receiver
        self.__query = query

    def execute(self):
        self.__receiver.get_event_user(self.__query)