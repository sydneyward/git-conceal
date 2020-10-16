#!/bin/bash

tar xfvz $1

input="files.txt"
while IFS= read -r line
do
  # python tokenizer.py $line
  echo "Tokenize $line"
done < "$input"