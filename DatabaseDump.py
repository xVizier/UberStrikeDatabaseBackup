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
<<<<<<< HEAD
MongoDump = 'mongodump --host localhost:27017 --username uber --password admin --authenticationDatabase admin'
try:
    os.system(MongoDump)
=======

try:
    os.system('cmd /k "mongodump --host localhost:27017 --username uber --password admin --authenticationDatabase admin"')
>>>>>>> 72d9e27aeb6df0accdf45ef41525900a9c4ae581
except:
    print('Could not execute MONGODUMP command')
# Opens CMD and Runs the MongoDump Command.
