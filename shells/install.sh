#!/bin/bash
sudo apt install python3.12-venv
python3 -m venv taxienv

source taxienv/bin/activate

pip install -r requirements.txt