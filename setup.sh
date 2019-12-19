!#/usr/bin/env bash

pip install tensorflow==2.0
pip install keras

sudo apt-get install unzip

unzip data.zip
make clean
make
