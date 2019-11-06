from subprocess import Popen, PIPE
from os import path

def run_git_command(command):
    
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

def main():
    print(path.curdir)
    print("type 0 to exit")
    command = 1
    while(command != '0'):
        command = input('Please type a git command:')
        run_git_command(command)

if __name__ == "__main__":
    main()
