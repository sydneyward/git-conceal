#!/bin/sh

tar xfz $1
echo ""
python secret_detector.py $2
