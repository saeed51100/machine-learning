
run this commands in project directory:

# create the projects virtual environment
# The second argument is the location to create the virtual environment.
# Generally, you can just create this in your project and call it .venv.
# venv will create a virtual Python installation in the .venv folder.
1- python3 -m venv .venv

# activate the virtual environment
# Before you can start installing or using packages in your virtual environment
# you’ll need to activate it. Activating a virtual environment will put the virtual
# environment-specific python and pip executables into your shell’s PATH.
2- source .venv/bin/activate

# To confirm the virtual environment is activated, check the location of your Python interpreter:
3- which python

4- pip install -r /path/to/requirements.txt

# If you want to switch projects or leave your virtual environment, deactivate the environment:
5- deactivate