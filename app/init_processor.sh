#!/bin/bash

tar xfvz $1

python secret_detector.py $2
