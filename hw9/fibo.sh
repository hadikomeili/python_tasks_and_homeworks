#!/bin/bash
echo 'a bash scrypt for create fibonacci sequence'
echo 'enter a number: '
read number
num1=0
num2=1
echo 'Fibonacchi series is:'

for (( i=0; i<number; i++ ))
do
	echo $num1
	fn=$((num1+num2))
	num1=$num2
	num2=$fn
done

