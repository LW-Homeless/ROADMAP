import requests
import pandas as pd

from tabulate import tabulate
from colorama import init, Fore


class APIGithub:

    def __init__(self):
        self.__headers = ''
        self.__response = ''
        self.__json = []

    def get_event_user(self, query):

        init()

        self.__headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                        'AppleWebKPushEventit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'}

        self.__response = requests.get(query, headers=self.__headers)

        if len(self.__response.json()) == 0:
            print(Fore.RED + "[i] No data to show")

        elif self.__response.status_code == 200:

            for p in self.__response.json():
                self.__json.append({'Event': p['type'], 'Repo Name': p['repo']['name']})

            df = pd.DataFrame(self.__json).groupby(['Event', 'Repo Name']).size().reset_index(name="Event Count")

            table = tabulate(df, headers="keys", tablefmt="simple_grid", showindex=False)

            print(Fore.YELLOW + table)
        elif self.__response.status_code == 404:
            print(Fore.RED + "[X] Status code response: 400")
