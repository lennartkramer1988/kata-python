# kata-python

# Verify if you have python 3 installed

You can try both `python --version` or `python3 --version`

## Download and Install python 3

1. You can find a [Python 3.10](https://www.python.org/downloads/release/python-3100/) download suitable for your system.
2. Using homebrew on a MacOS system `brew install python`

## Install the python package manager pip
This is the package manager used for python (like maven or gradle)
1.  `python3 -m pip install -U --force-reinstall pip`

# Setting up virtual environment and installing dependencies

To prevent packages / project dependencies from being installed for all your projects a virtual environment is required.
This virtual environment is a fresh python install with no other libraries installed. 
This helps prevent version conflicts between your projects (project A might use version 1 and project B might use version 2 of the same library)

## Steps

1. Install virtualenv with the pip package manager `pip install virtualenv`
2. verify your installation `virtualenv --version`
3. Go to the project root `cd kata-python`
4. Create the virtual environment `virtualenv venv` (the name venv can be anything however it is common practice to use venv)
5. Switch to the virtual environment `source venv/bin/activate`
6. Install all packages in the requirements.txt file `python3 -m pip install -r requirements.txt`

# The Kata







# Python basics cheat sheet





