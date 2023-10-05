import os
from github import Github

CurrentDirectory = os.getcwd()


GitAdd = 'git add .'
GitCommit = 'git commit -m "Routine Backup"'
GitBranch = 'git branch -M main'
GitPush = 'git push -u origin main'
GitPull = 'git pull'

print(CurrentDirectory)

try:
    os.system(GitPull)
except:
    print("Couldn't Execute Command.")
try:
    os.system(GitAdd)
except:
    print("Couldn't Execute Command.")

try:
    os.system(GitCommit)
except:
    print("Couldn't Execute Command.")

try:
    os.system(GitBranch)
except:
    print("Couldn't Execute Command.")

try:
    os.system(GitPush)
except:
    print("Couldn't Execute Command.")