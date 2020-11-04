#!/bin/sh

tar xfvz $1
echo ""
python secret_detector.py $2
