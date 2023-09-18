#!/bin/bash

echo "Please enter a Directory path to display the sha256sum of its hidden files"
read path
cd $path
find $path -type f -name ".*" -ls | cut -d "/" -f 4 > $path/Issa.txt
file=$(cat $path/Issa.txt)
for line in $file
do
echo -e "$line\n" | sha256sum | cut -d " " -f 1
done
