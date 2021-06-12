#i/bin/bash

echo 'this is a program for sunset and sunrise for today'
echo 'enter your location latitude?'
read lat
echo 'enter your location longitude?'
read lng
curl 'https://api.sunrise-sunset.org/json?lat='$lat'&lng='$lng | python3 -m json.tool
