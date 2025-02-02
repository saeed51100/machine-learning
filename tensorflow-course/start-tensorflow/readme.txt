
1- install requirements of tensor from: https://www.tensorflow.org/install/pip

    # check if >= 525.60.13 nvidia driver is installed in software updater else goto step 2.
    # install gcc
        sudo apt install build-essential
        gcc --version
    # download cuda runfile from: https://developer.nvidia.com/cuda-downloads
    # use this link to install runfile: https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html#ubuntu-x86-64-run

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
     pip install --upgrade pip
     # For GPU users
     pip install tensorflow[and-cuda]
     # For CPU users
     pip install tensorflow
     .
     .
     .
     and other commands in the above link.

9-  numpy and keras is installed with tensorflow.
10- pip install pandas
11- pip install scikit-learn


# If you want to switch projects or leave your virtual environment, deactivate the environment:
9- deactivate