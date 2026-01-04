#!/bin/bash

pip install --force-reinstall git+https://github.com/jaraco/path.git --upgrade -t ./local_lib  > install.log 2>&1
pip install --upgrade pip
pip -V
if grep -q "Successfully installed" install.log ; then
    PYTHONPATH=./local_lib python3 my_program.py
else
    echo "Error"
fi