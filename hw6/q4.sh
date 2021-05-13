#!/bin/bash
echo 'Welcom. This is a program for reading files.'
echo 'please enter the file name:'
read file_name
if [[ -f $file_name ]]
then
	tail -10 $file_name
else
	echo "File dose not exist!!!"
fi
