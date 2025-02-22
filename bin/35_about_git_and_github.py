"""
Git: Version Control System
"""

# --------
# Create git repository in laptop
# --------
# step-1: download git-software and install
#   https://git-scm.com/downloads
#
# step-2: make python_training as git-repository
#       - 1. open terminal/cmd-prompt
#       - 2. cd c:\python_training
#       - 3. git init
#
# step-3: NOW python_training folder is git repository
#
# step-4: add all files & folders to git repository
#       - git status
#       - git add bin flask_rest_api log programs Readme.txt
#       - git commit -m "adding all files and folders to git repository"
#################


# --------
# Create github repository
# --------
# Step-1: Create account in https://github.com/
#
# Step-2: create new repository "python_training" in github
#
# Step-3: DONE
#################

# --------
# Link local repository (python_training folder in laptop)
#   with
#   github repository
# --------
# Step-1:
#   git remote add origin https://github.com/mahadevaprabhug/python_training_9.git
#
# DONE
#################

# --------
# PUSH all the code from
#  local repository (python_training folder in laptop)
#   to
#   github repository
# --------
# Step-1:
#   git push -u origin master
#################

# --------
# PULL trainer code from github
# --------
# Step-1:
#   create new directory "trainer_code"
#
# Step-2:
#   make trainer_code as git hub repository
#       - 1. open terminal/cmd-prompt
#       - 2. cd c:\trainer_code
#       - 3. git init
#
# step-3: NOW trainer_code folder is git repository
#
# Step-4: Link trainer_code repository with trainer-github repository
#   git remote add origin https://github.com/mahadevaprabhug/python_training_9.git
#
# Step-5: pull the code
#   git pull origin master
#
# Step-6: Now you should have all the files in trainer_code directory
#################