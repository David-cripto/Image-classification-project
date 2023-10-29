#!/bin/bash

apt-get update

apt-get install -y python3-pip

pip install -r requirements.txt --break-system-packages
