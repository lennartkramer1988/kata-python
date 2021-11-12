# kata-python

# Verify if you have python 3 installed

You can try both `python --version` or `python3 --version`

## Download/Install python 3

1. You can find a [Python 3.10](https://www.python.org/downloads/release/python-3100/) download suitable for your system.
2. Using homebrew on a MacOS system `brew install python`

## Install Pip 
This is the package manager used for python (like maven or gradle)
1.  `python3 -m pip install -U --force-reinstall pip`

# Virtual environment

To prevent packages / project dependencies from being installed for all your projects a virtual environment is required.
This virtual environment is a fresh python install with no other libraries installed. 
This helps prevent version conflicts between your projects (project A might use version 1 and project B might use version 2 of the same library)

## Installing venv


`python3 -m venv python-kata`
`python3 -m pip install -r requirements.txt`
