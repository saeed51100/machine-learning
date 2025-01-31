
run this commands in project directory:

1- install requirements of tensor from: https://www.tensorflow.org/install/pip

    # Before installing the Nvidia driver, you need to install the Linux header:
    # https://askubuntu.com/questions/75709/how-do-i-install-kernel-header-files
        sudo apt-get install linux-headers-$(uname -r)

    Then:

    a- NVIDIA® GPU drivers
    b- CUDA® Toolkit 12.3.
    c- cuDNN SDK 8.9.7.

2- set the pycharm terminal in your project folder.

# create the projects virtual environment
3- python3 -m venv .venv

# activate the virtual environment
4- source .venv/bin/activate

5- set the interpreter to: .venv/bin/python3.12 //(latest version)

# To confirm the virtual environment is activated, check the location of your Python interpreter:
6- open a new terminal then:
7- which python

8- install tensorflow from: https://www.tensorflow.org/install/pip


# If you want to switch projects or leave your virtual environment, deactivate the environment:
9- deactivate