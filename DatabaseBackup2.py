import os
from github import Github
from datetime import date
# Date is used for the Folder Name
GetDate = date.today()
Today=str(GetDate)
# Converted to String.
FormattedDate = Today.replace('-', '')
# Removes the '-' from the date.

FolderName = "Backup_"+FormattedDate
# Assigns the Folder Name to be created
CurrentDirectory = os.getcwd()
# Retrieves the Current Directory from System
os.makedirs(FolderName)
# Creates the Backup Folder with date as unique identifier
os.chdir(FolderName)
# Changes the Directory to the current folder.
print(CurrentDirectory)
try:
    os.system('cmd /k "mongodump --host localhost:27017 --username uber --password admin --authenticationDatabase admin"')
except:
    print('Could not execute MONGODUMP command')
# Opens CMD and Runs the MongoDump Command.

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