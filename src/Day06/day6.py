"""
Day 6 of python learning 
--------------------------
Author:     Akshay
Date:       23/04/2023
--------------------------
"""

# Dictonary 

some_dict = {"akshay": 23, "john": 20, "hrithik": 17, "varun": 14}

def print_dict(dictionary):
	for i, j in dictionary.items():
		print(f'{i} : {j}', end=" | ")
		# print('\n{}: {}'.format(i, j))	

print_dict(some_dict)