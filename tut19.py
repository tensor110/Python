# Virtual Environment

# virtual environment is a tool used to isolate specific Python environments on a single machine. allowing you to work
# on multiple projects with different dependencies and packages without conflicts. This can be especially useful when
# working on projects that have conflicting package versions or packages that are not compatible with each other.

# To create a virtual Environment
# python -m venv envname



# To activate the vitual Environment

# source myenvname/Scripts/activate.bat (for terminal)
# source myenvname/Scripts/activate.ps1 (for powershell)



# To deactivate virtual environment 
# deactivate



# To know all the packages and version
# pip freeze



# To print all packages and versions in a text file
# pip freeze> requirements.txt



# To install all the packages listed in the tetx file
# pip install -r requirements.txt