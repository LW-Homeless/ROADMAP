import argparse

from colorama import Fore, init

from model.APIGithub import APIGithub
from model.CommandInvoker import CommandInvoker
from model.Command import GetEventUser


class GitHubActivity:

    @staticmethod
    def main():

        parser = argparse.ArgumentParser(description="GitHub User Activity v1.0.0")
        parser.add_argument("user", type=str, help="Input the Github-user")

        arg = parser.parse_args()

        api = APIGithub()
        invoker = CommandInvoker()
        

        init()

        print(Fore.GREEN + "Github-Username: " + arg.user)
        invoker.execute_command(GetEventUser(api, f"https://api.github.com/users/{arg.user}/events"))


if __name__ == '__main__':
    GitHubActivity.main()
