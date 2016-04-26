#!/bin/bash

input_file="$1"
output_file="$input_file".md

prefix="xxx<"
postfix=">ooo"
replaced_prefix="<img src='.\/resource\/icons\/"
replaced_postfix=".png' height='35px'>"

sed -e "s/$prefix/$replaced_prefix/g" -e "s/$postfix/$replaced_postfix/g" $input_file > $output_file

echo "Ouput: $output_file"
echo "Done!"
