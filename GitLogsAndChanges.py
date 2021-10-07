import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from typing import re
from pydriller import Repository
from CONST import *


filenames = os.listdir(ABS_REPO_PATH)  # get all files' and folders' names in the current directory

result = []
for filename in filenames:  # loop through all the files and folders
    if os.path.isdir(
            os.path.join(os.path.abspath(ABS_REPO_PATH), filename)):  # check whether the current object is a folder or not
        result.append(filename)
        print(filename)

result.sort()

file1name = os.path.join(ABS_SAVE_PATH, 'GIT_COMMITS.CSV')
file1 = open(file1name, 'w', encoding="utf-8")
header1 = '"PROJECT_ID", "COMMIT_HASH", "COMMIT_MESSAGE", "AUTHOR", "AUTHOR_DATE", "AUTHOR_TIMEZONE", "COMMITTER", "COMMITTER_DATE", "COMMITTER_TIMEZONE", "BRANCHES", "IN_MAIN_BRANCH", "MERGE", "PARENTS"\n'
file1.write(header1)

file2name = os.path.join(ABS_SAVE_PATH, 'GIT_COMMITS_AND_CHAGES.CSV')
file2 = open(file2name, 'w', encoding="utf-8")
header2 = '"PROJECT_ID", "FILE", "COMMIT_HASH", "DATE", "COMMITTER_ID", "LINES_ADDED", "LINES_REMOVED", "NOTE"\n'
file2.write(header2)

for index, project_dir in enumerate(result): #go over all projects
    project_name=project_dir
    projectDirAbsPath = os.path.join(ABS_REPO_PATH, project_dir)
    projectSaveAbsPath = os.path.join(ABS_SAVE_PATH, project_dir)
    filep1name = os.path.join(projectSaveAbsPath, 'GIT_COMMITS.csv')
    filep2name = os.path.join(projectSaveAbsPath, 'GIT_COMMITS_AND_CHANGES.csv')
    filep1 = open(filep1name, 'w', encoding='utf-8')
    filep2 = open(filep2name, 'w', encoding='utf-8')
    filep1.write(header1)
    filep2.write(header2)
    print('analyzing project '+ project_dir)
    # Go over all commits and modifications
    for commit in Repository(projectDirAbsPath).traverse_commits():
        line1='"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}"\n'.format("org.apache:"+project_dir,
                                                                        commit.hash.replace('\n',' '), 
                                                                        commit.msg.replace('\n', ' ')
                                                                                .replace('"', '')
                                                                                .replace(',', ' '),
                                                                        commit.author.name.replace('\n', ' '), 
                                                                        commit.author_date,
                                                                        commit.author_timezone,
                                                                        commit.committer.name.replace('\n', ' '), 
                                                                        commit.committer_date,
                                                                        commit.committer_timezone,
                                                                        commit.branches,
                                                                        commit.in_main_branch,
                                                                        commit.merge,
                                                                        commit.parents)
        file1.write(line1)
        filep1.write(line1)
        for mod in commit.modified_files:
            line2='"{}","{}","{}","{}","{}","{}","{}","{}"\n'.format("org.apache:"+project_dir,
                                                                        mod.filename,
                                                                        commit.hash.replace('\n',' '), 
                                                                        commit.committer_date, 
                                                                        commit.author.name.replace('\n', ' '), 
                                                                        mod.added_lines,
                                                                        mod.deleted_lines, 
                                                                        commit.msg.replace('\n', ' ')
                                                                                .replace('"', '')
                                                                                .replace(',', ' '))
            file2.write(line2)
            filep2.write(line2)

    filep1.close()
    filep2.close()

file1.close()
file2.close()
