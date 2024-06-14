#!/usr/bin/env python

#Taking integer inputs from users for the calculations. I made a for loop for seven times as I wanted to make seven calculations
for i in range(7):
	Fahrenheit = int(input("enter temperature in Fahrenheit: "))
#Printing the Celsius value using the given formula
	Celsius = (Fahrenheit - 32) * 5 / 9
	print(Celsius)
