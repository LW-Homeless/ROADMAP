Sample solution for the [GitHub-User-Activity](https://roadmap.sh/projects/github-user-activity) challenge from [roadmap.sh](https://roadmap.sh)

# GitHub User Activity
In this project, you will build a simple command line interface (CLI) to fetch the recent activity of a GitHub user and display it in the terminal. This project will help you practice your programming skills, including working with APIs, handling JSON data, and building a simple CLI application.

# Requirements
The application should run from the command line, accept the GitHub username as an argument, fetch the user’s recent activity using the GitHub API, and display it in the terminal. The user should be able to:

- Provide the GitHub username as an argument when running the CLI.
`python github-activity <username>`

- Fetch the recent activity of the specified GitHub user using the GitHub API. You can use the following endpoint to fetch the user's activity:
 https://api.github.com/users/ **username** /events
 Example:  https://api.github.com/users/ **LW-Homeless** /events

# Solution
- Programming language: Python 3.11.3.
- Type of programming: object-oriented programming (OOP).
- Design pattern: Command Behavior Design Pattern **Command**.

The Command design pattern has the following structure.
![image](https://github.com/LW-Homeless/roadmap/blob/main/backend/task-tracker/structure.png) 
# How to use
Install the modules Pandas, colorama and tabutate with the following command:
pip install tabulate
pip install pandas 
pip install colorama
pip install requests

Finally, run the following command:
`python github-activity.py username`

![video](https://github.com/LW-Homeless/roadmap/blob/main/backend/GitHub-User-Activity/video.gif)
