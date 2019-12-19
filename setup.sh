!#/usr/bin/env bash

pip install tensorflow==2.0
pip install keras

unzip data.zip
make clean
make
