1- sudo apt update && sudo apt upgrade

2- install requirements of tensor from: https://www.tensorflow.org/install/pip

    # check if >= 525.60.13 nvidia driver is installed in software updater else goto step 2.
    # install gcc
        sudo apt install build-essential
        gcc --version
    # download and install cuda deb(local) from:
        https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_local

    a- NVIDIA® GPU drivers
    b- CUDA® Toolkit 12.3.
    c- cuDNN SDK 8.9.7.

3- set the pycharm terminal in your project folder.

# create the projects virtual environment
4- python3 -m venv .venv

# activate the virtual environment
5- source .venv/bin/activate

6- set the interpreter to: .venv/bin/python3.12 //(latest version)

# To confirm the virtual environment is activated, check the location of your Python interpreter:
7- open a new terminal then:
8- which python

9- Prepare pip
     pip install --upgrade pip
     pip --version

10- install tensorflow from: https://www.tensorflow.org/install/pip
     # For GPU users
     pip install tensorflow[and-cuda]
     # For CPU users
     pip install tensorflow
     .
     .
     .
     and other commands in the above link.

11- numpy and keras is installed with tensorflow.
12- pip install pandas
13- pip install scikit-learn


# If you want to switch projects or leave your virtual environment, deactivate the environment:
14- deactivate