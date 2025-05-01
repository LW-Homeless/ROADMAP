from prompt_toolkit.shortcuts import set_title
from Screen.Screen import app


class Main:
    @staticmethod
    def main():
        set_title("Weather API")
        app.run()


if __name__ == '__main__':
    Main.main()
