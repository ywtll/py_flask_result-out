#!/bin/bash
export FLASK_APP=app.py
export FLASK_ENV=development
export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8
nohup python3 -m flask run -h0.0.0.0 -p443 &
