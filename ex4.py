#!/usr/bin/env python

#Task 1: just printing details
print("my name is Rehar Subba")
print("I am from Bhutan")
print("I am studying Graduate Certificate in IT at Murdoch")

#Task 2: units information
# I created a dictionary to list out my units and their code as key, value pairs. i thought this may be useful some day
units = {
		"ICT521" : "IT Professional Practice",
		"ICT581" : "Information Systems Principles and Practive",
		"ICT582" : "Python Programming Principles and Practice",
		"ICT583" : "Data Science Applications"
}

print("My units are: ")

# for loop to print out my units. The loop iterates over my dictionary and assigns the values of the items to key and value. The print function inside the 
#for loop uses tf-string expression to place the keys and values
for key, value in units.items():
	print(f"{key}: {value}")
