#i/bin/bash

echo "play mp3 files and mark them"
echo "enter a directory: "
read directory
cd $directory
mpg123 -Z *.mp3
echo "what mark you did to this song?"
read mark


