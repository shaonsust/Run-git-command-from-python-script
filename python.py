import requests
from bs4 import BeautifulSoup
import html5lib
from subprocess import Popen, PIPE
from os import path
import sys

# url = 'https://www.premierleague.com/stats/top/players/goals?se=-1&cl=-1&iso=-1&po=-1?se=-1';
# response = requests.get(url)
# soup = BeautifulSoup('span', 'html.parser')
# print(response.content)
def run_git_command(command):
    git_command = ['/usr/bin/git', command]
    repo = path.dirname('/var/www/html/biznet/')
    repo = path.dirname('/home/goku/Goku/WorkingPlace/Javascript/')

    git_query = Popen(command.split(), cwd=repo, stdout=PIPE, stderr=PIPE)
    (git_status, error) = git_query.communicate()

    try:
        output = bytes(git_status).decode()
        error = bytes(error).decode()
        if output:
            print("output: " + output)
        if error:
            print("error: " + error)
    except TypeError:
        print()

# if git_query.poll() == 0:
    # print(git_status)
def main():
    print(path.curdir)
    print("type 0 to exit")
    command = 1
    while(command != '0'):
        command = input('Please type a git command:')
        run_git_command(command)

if __name__ == "__main__":
    main()
