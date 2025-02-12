"""
Implement concrete command and pass call to one logical business object.
"""


from .ICommand import ICommand


class GetEventUser(ICommand):
    """
    Class: GetEventUser
    Description: Implement command to get GitHub User's event
    """
    def __init__(self, receiver, query):
        self.__receiver = receiver
        self.__query = query

    def execute(self):
        self.__receiver.get_event_user(self.__query)
