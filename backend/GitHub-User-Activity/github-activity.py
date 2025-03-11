import argparse

from colorama import Fore, init

from model.APIGithub import APIGitHub
from model.CommandInvoker import CommandInvoker
from model.Command import GetEventUser


class GitHubActivity:
    """
    Class: GitHubActivity
    Description: Is responsible run the application
    """
    @staticmethod
    def main():
        """
        Description:
            Initialized the application
        """
        parser = argparse.ArgumentParser(description="GitHub User Activity v1.0.0")
        parser.add_argument("user", type=str, help="Input the Github-user")

        arg = parser.parse_args()

        api = APIGitHub()
        invoker = CommandInvoker()
        

        init()

        print(Fore.GREEN + "Github-Username: " + arg.user)
        invoker.execute_command(GetEventUser(api, f"https://api.github.com/users/{arg.user}/events"))


if __name__ == '__main__':
    GitHubActivity.main()
