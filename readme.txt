
run this commands in project directory:

1- set the pycharm terminal in your project folder.

# create the projects virtual environment
# The second argument is the location to create the virtual environment.
# Generally, you can just create this in your project and call it .venv.
# venv will create a virtual Python installation in the .venv folder.
2- python3 -m venv .venv

# activate the virtual environment
# Before you can start installing or using packages in your virtual environment
# you’ll need to activate it. Activating a virtual environment will put the virtual
# environment-specific python and pip executables into your shell’s PATH.
3- source .venv/bin/activate

4- set the interpreter to: .venv/bin/python3.12 //(latest version)

# To confirm the virtual environment is activated, check the location of your Python interpreter:
5- open a new terminal then:
6- which python

7- pip install -r requirements.txt

# If you want to switch projects or leave your virtual environment, deactivate the environment:
8- deactivate