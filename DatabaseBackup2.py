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
#os.makedirs(FolderName)
# Creates the Backup Folder with date as unique identifier
#os.chdir(FolderName)
# Changes the Directory to the current folder.

#try:
#    os.system('cmd /k "mongodump --host localhost:27017 --username uber --password admin --authenticationDatabase admin"')
#except:
#    print('Could not execute MONGODUMP command')
# Opens CMD and Runs the MongoDump Command.

#Token = "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"

#Git = Github(Token)

#for repo in Git.get_user().get_repos():
#    print("Repo:", repo.name)

#repo = Git.get_repo("xVizier/UberStrikeDatabaseBackups")
#try:
#    os.system('cmd k/ "cd C:\Program Files\Git"')
#except:
#    print("Couldn't Execute Command.")

#try:
#    os.system('cmd k/ "git-bash.exe"')
#except:
#    print("Couldn't Execute Command.")
GitAdd = 'git add .'
GitCommit = 'git commit -m "Routine Backup"'
GitBranch = 'git branch -M main'
GitPush = 'git push -u origin main'
GitPull = 'git pull'
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